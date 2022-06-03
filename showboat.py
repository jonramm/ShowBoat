# Sources:
# Packaging app with pyinstaller:
# https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/
# https://github.com/pyinstaller/pyinstaller/issues/1826
# Web scraping:
# https://mechanize.readthedocs.io/en/latest/
# # Haversine formula
# https://www.geeksforgeeks.org/program-distance-two-points-earth/
# PyQt threading
# https://realpython.com/python-pyqt-qthread/
# PyQt basics:
# https://www.youtube.com/watch?v=rZcdhles6vQ&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY
# Mouse hover for table widget
# https://stackoverflow.com/questions/20064975/how-to-catch-mouse-over-event-of-qtablewidget-item-in-pyqt

import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic
import sys
import os
import io
import folium
import requests
from time import time
import urllib
from bs4 import BeautifulSoup
import mechanize
from math import radians, cos, sin, asin, sqrt
import resources

# provide windows with different application id so we can display a custom taskbar icon 
try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'ShowBoat.1.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

# provide relative filepaths for assets
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    bundle_dir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
GUI_PATH = os.path.join( bundle_dir, 'showboat.ui' )
IMG_PATH = os.path.join( bundle_dir, 'showboat_white_cropped.png' )
LOGO_PATH = os.path.join( bundle_dir, 'showIcon.ico' )

#######################################################################################
#                                                                                     #
# Define secondary threads for making API calls                                       #
#                                                                                     #
#######################################################################################

class VideoSearchThread(QThread):
    """
    Creates a thread object for running calls to teammate's microservice. API calls run in thread
    will not freeze the app GUI.
    """
    authResult = pyqtSignal(object)

    def __init__(self, artist):
        QThread.__init__(self)
        self.artist = artist

    def video_search(self):
        """
        Takes an artist name as a parameter and calls the YouTube scraper API endpoint. Updates
        display widgets with returned data.
        """
        obj = {"name": self.artist, "type": "popular"}
        response = requests.post('https://youtube-scraper-microservice.herokuapp.com/videos', json=obj)
        data = response.json()
        if response.status_code != 200 or len(data) < 2:
            self.authResult.emit(False)
        else:
            self.authResult.emit(data)

    def run(self):
        self.video_search()

class DateConversionThread(QThread):
    """
    Creates a thread object for running calls to teammate's microservice. API calls run in thread
    will not freeze the app GUI.
    """
    authResult = pyqtSignal(object)

    def __init__(self, date_arr):
        QThread.__init__(self)
        self.date_arr = date_arr

    def date_convert(self):
        """
        Iterates through array of dates to be converted and makes individual calls to
        teammate's microservice.
        """
        result = []
        for date in self.date_arr:
            res = requests.get(f"https://mstagg.pythonanywhere.com/{date}/long")
            newDate = res.text
            result.append(newDate)
        # emits result array to be picked up by main thread
        self.authResult.emit(result)

    def run(self):
        self.date_convert()

class AutocompleteThread(QThread):
    """
    Creates a thread object for running calls to AudioDB API. API calls run in thread
    will not freeze the app GUI.
    """
    authResult = pyqtSignal(object)

    def __init__(self, search_string):
        QThread.__init__(self)
        self.search_string = search_string

    def scrape(self):
        """
        Takes a search string and scrapes the AudioDB website to return a list of artist names.
        Returns the names as an array.
        """
        URL ="https://www.theaudiodb.com/browse.php"
        br = mechanize.Browser()
        response = br.open(URL)
        br.form = list(br.forms())[0] 
        control = br.form.controls[0]
        control.value = self.search_string # insert search string into form
        response = br.submit()
        data = response.read()
        soup = BeautifulSoup(data, "html.parser")
        results = soup.find_all("a")
        nameArr = []
        for a in results:
            if '/artist' in a['href']:
                nameArr.append(a.getText())
        self.authResult.emit(nameArr)

    def run(self):
        self.scrape()

#######################################################################################
#                                                                                     #
# Define main window class                                                            #
#                                                                                     #
#######################################################################################

class UI(QtWidgets.QMainWindow):

    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi(GUI_PATH, self)
        self.previousSearch = ''
        self.currentSearch = ''
        self.currentTab = 0
        self.channelUrl = ''
        self.date_arr = []
        self.currentArtist = ''
        self.curDates = []
        self.searchedArtists = "Artists searched:"
        self.completerThreadFinished = True
        self.current_hover = [0, 0]


#######################################################################################
#                                                                                     #
# Define Widgets                                                                      #
#                                                                                     #
#######################################################################################

        # Initialize status bar
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setFont(QFont("Ebrima", 12))
        self.statusBar.showMessage(self.searchedArtists)

        # Tabs
        self.tabs = self.findChild(QtWidgets.QTabWidget, "tabs")
        self.tabs.setCurrentIndex(self.currentTab)
        self.homeTab = self.findChild(QtWidgets.QWidget, "homeTab")
        self.tourDatesTab = self.findChild(QtWidgets.QWidget, "tourDatesTab")
        self.mapTab = self.findChild(QtWidgets.QWidget, "mapTab")
        self.videoTab = self.findChild(QtWidgets.QWidget, "videoTab")
        self.infoTab = self.findChild(QtWidgets.QWidget, "infoTab")

        # Home
        self.bandPhotoLabel = self.findChild(QtWidgets.QLabel, "bandPhotoLabel")
        self.homeArtistLabel = self.findChild(QtWidgets.QLabel, "homeArtistLabel")
        self.homeBioPlainTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "homeBioPlainTextEdit")
        self.bandSearchLineEdit = self.findChild(QtWidgets.QLineEdit, "bandSearchLineEdit")
        self.completer = QtWidgets.QCompleter()
        self.model = QtCore.QStringListModel()
        self.completer.setModel(self.model)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.completer.popup().setStyleSheet("font-size: 20;")
        self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.bandSearchLineEdit.setCompleter(self.completer)
        self.lastSearchButton = self.findChild(QtWidgets.QPushButton, "lastSearchButton")
        self.searchButton = self.findChild(QtWidgets.QPushButton, "searchButton")
        self.searchButton.setCursor(Qt.QCursor(QtCore.Qt.PointingHandCursor))
        self.lastSearchButton.setCursor(Qt.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoPhotoLayout = self.findChild(QtWidgets.QVBoxLayout, "logoPhotoLayout")

        # Tour Dates

        self.showsTableWidget = self.findChild(QtWidgets.QTableWidget, "showsTableWidget")
        self.artistTourLabel = self.findChild(QtWidgets.QLabel, "artistTourLabel")
        self.showsTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.showsTableWidget.horizontalHeader().setFont(QFont("Ebrima", 14))
        self.showsTableWidget.setColumnWidth(0,166)
        self.showsTableWidget.setColumnWidth(1,396)
        self.showsTableWidget.setColumnWidth(2,385)
        self.showsTableWidget.setColumnWidth(3,76)
        self.showsTableWidget.setMouseTracking(True)

        # Map
        self.mapMapContainer = self.findChild(QWebEngineView, "mapMapContainer")
        coordinates = (27.03992362079509, -22.920434372492934)
        self.initializeMap(coordinates, 2)
        self.citySearchButton = self.findChild(QtWidgets.QPushButton, "citySearchButton")
        self.clearCityButton = self.findChild(QtWidgets.QPushButton, "clearCityButton")
        self.citySearchButton.setCursor(Qt.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearCityButton.setCursor(Qt.QCursor(QtCore.Qt.PointingHandCursor))
        self.citySearchInput = self.findChild(QtWidgets.QLineEdit, "citySearchInput")
        self.miles50Radio = self.findChild(QtWidgets.QRadioButton, "miles50Radio")
        self.miles100Radio = self.findChild(QtWidgets.QRadioButton, "miles100Radio")
        self.miles250Radio = self.findChild(QtWidgets.QRadioButton, "miles250Radio")
        self.mapMapHeaderLabel = self.findChild(QtWidgets.QLabel, "mapMapHeaderLabel")

        # Video
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.video0 = self.findChild(QWebEngineView, "video0")
        self.video1 = self.findChild(QWebEngineView, "video1")
        self.video2 = self.findChild(QWebEngineView, "video2")
        # put video widgets in a dict for easy iteration
        self.video_dict = {
            "video0": self.video0,
            "video1": self.video1,
            "video2": self.video2
        }
        self.radioButtonPopular = self.findChild(QtWidgets.QRadioButton, "radioButtonPopular")
        self.radioButtonNewest = self.findChild(QtWidgets.QRadioButton, "radioButtonNewest")
        self.radioButtonOldest = self.findChild(QtWidgets.QRadioButton, "radioButtonOldest")
        self.videoSeeMoreButton = self.findChild(QtWidgets.QPushButton, "videoSeeMoreButton")
        self.videoSeeMoreButton.setCursor(Qt.QCursor(QtCore.Qt.PointingHandCursor))

#######################################################################################
#                                                                                     #
# Connect functions to widgets                                                        #
#                                                                                     #
#######################################################################################

        self.searchButton.clicked.connect(lambda: self.artist_search('search'))
        self.lastSearchButton.clicked.connect(lambda: self.artist_search('previous'))
        self.showsTableWidget.itemDoubleClicked.connect(self.link_clicked)
        self.radioButtonPopular.toggled.connect(lambda: self.video_refresh('popular'))
        self.radioButtonNewest.toggled.connect(lambda: self.video_refresh('newest'))
        self.radioButtonOldest.toggled.connect(lambda: self.video_refresh('oldest'))
        self.videoSeeMoreButton.clicked.connect(self.artistChannelRedirect)
        self.citySearchButton.clicked.connect(lambda: self.searchByCity(self.citySearchInput.text()))
        self.clearCityButton.clicked.connect(self.clearCity)
        self.bandSearchLineEdit.textChanged.connect(lambda: self.auto_complete(self.bandSearchLineEdit.text()))
        self.showsTableWidget.cellEntered.connect(self.cellHover)

        # show the app
        self.show()

#######################################################################################
#                                                                                     #
# Define functions                                                                    #
#                                                                                     #
#######################################################################################

#####################################################
#                                                   #
# General                                           #
#                                                   #
#####################################################

    def updateWidgets(self, data):
        """
        Takes an artist data object, updates the display widgets, and calls the tour search
        and video search methods..
        """
        self.homeBioPlainTextEdit.clear()
        self.homeBioPlainTextEdit.insertPlainText(data['bio'])
        self.set_photo(data['img_url'])
        self.tour_search(data['artist'])
        # creates separate thread for video search microservice calls   
        self.video_search(data['artist'])
        self.currentArtist = data['artist']
        self.previousSearch = self.currentSearch
        if self.currentArtist not in self.searchedArtists:
            if self.searchedArtists[-1] == ":":  
                self.searchedArtists += f" {data['artist']}"
            else:
                self.searchedArtists += f", {data['artist']}"
        self.currentSearch = data['artist']
        self.homeArtistLabel.setText(self.currentArtist)
        self.statusBar.showMessage(self.searchedArtists)
        self.artistTourLabel.setText(f"\u261D {self.currentArtist} tour dates \u261D")
        self.mapMapHeaderLabel.setText(f"Click a marker on the map to see {self.currentArtist} show details")

    def errorBox(self, msgString):
        """
        Takes a message string and displays an error box popup.
        """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(msgString)
        x = msg.exec_()

    def loadSplash(self):
        """
        Returns a 'loading' splash screen object with a custom image.
        """
        pixmap = QPixmap(IMG_PATH)
        pixmapScaled = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        splash_screen = QtWidgets.QSplashScreen(pixmapScaled)
        splash_screen.setFont(QFont("Ebrima", 20))
        splash_screen.showMessage('Loading...', color=QtGui.QColor(200, 47, 101))
        return splash_screen

    def keyPressEvent(self, event):
        """
        Handles user key presses.
        """
        if event.key() == 16777220 or event.key() == 16777221:
            if self.tabs.currentIndex() == 0:
                self.artist_search('key_press')
            elif self.tabs.currentIndex() == 2:
                self.searchByCity(self.citySearchInput.text())

    def link_clicked(self, item):
        """
        Takes a tour table cell as a parameter and uses its stored tooltip data to 
        link to a Songkick webpage containing either venue or tour date ticket info.
        """
        if item.toolTip():
            confirm = QtWidgets.QMessageBox()
            confirm.setWindowTitle("Confirm redirect")
            confirm.setText('Link will open in your browser...do you wish to proceed?')
            confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            confirm.exec_()
            if confirm.standardButton(confirm.clickedButton()) == QtWidgets.QMessageBox.Yes:
                self.confirmation = 1
                webbrowser.open(item.toolTip())
            else:
                self.confirmation = 0

#####################################################
#                                                   #
# SEARCH tab                                        #
#                                                   #
#####################################################

    def artist_search(self, type):
        """
        Takes a search type (search button clicked or 'return' pressed) and calls the 
        artist search API endpoint. Updates display widgets with returned data.
        """
        if type == 'search' or type == 'key_press':
            value = self.bandSearchLineEdit.text()
            if not value:
                self.errorBox("Please enter an artist name")
                return
            obj = {"artist_search": value}
        else:
            value = self.previousSearch
            if not value:
                self.errorBox("Previous search unavailable")
                return
            obj = {"artist_search": value}
        splash_screen = self.loadSplash()
        splash_screen.show()
        app.processEvents()
        response = requests.post('https://showboat-rest-api.herokuapp.com/artist-search', data=obj)
        data = response.json()
        if data['artist']:
            self.updateWidgets(data)
        else:
            self.errorBox("Artist not found") 
        self.bandSearchLineEdit.setText("")
        splash_screen.close()

    def set_photo(self, img_url):
        """
        Takes an image url and creates a pixmap, then updates the artist photo
        display widget.
        """
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

    def auto_complete(self, search_string):
        """
        Takes a search string with the current text in the search bar. Creates a separate thread
        for non-blocking use of an AudioDB web scraper.
        """
        if self.completerThreadFinished:
            self.completerThreadFinished = False
            self.autoThread = AutocompleteThread(search_string)
            self.autoThread.authResult.connect(self.handleAutoResult)
            self.autoThread.finished.connect(self.on_finish)
            self.autoThread.start()

    def on_finish(self):
        """
        Sets boolean value for global completerThreadFinished variable so auto_complete() threads
        aren't piled on top of one another.
        """
        self.completerThreadFinished = True

    def handleAutoResult(self, result):
        """
        Takes result array and updates completer.
        """
        self.model.setStringList(result)
        self.completer.complete()
        self.autoThread.quit()

#####################################################
#                                                   #
# SHOWS tab                                         #
#                                                   #
#####################################################

    def tour_search(self, artist):
        """
        Takes an artist name as a parameter and calls the tour search API endpoint which pulls
        Songkick tour data from the web. Also calls teammate's date conversion microservice API
        endpoint. Updates display widgets with returned data.
        """
        self.initializeMap((27.03992362079509, -22.920434372492934), 2)
        obj = {"artist_search": artist}
        response = requests.post('https://showboat-rest-api.herokuapp.com/tour-search', data=obj)
        data = response.json()
        # hold dates data for later map manipulation
        self.curDates = data["events"]
        for obj in data["events"]:
            self.addPopUps(obj)
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())
        self.populateTourDateCells(data)
        # creates separate thread for date conversion microservice calls     
        self.date_conversion(self.date_arr)

    def populateTourDateCells(self, data):
        """
        Takes a data object and fills the table cells in the Tour Dates tab.
        """
        row = 0
        self.showsTableWidget.setRowCount(len(data["events"]))
        for date in data["events"]:
            # restructure date for API call to conversion microservice
            rawDate = date['start']['date']
            front = rawDate[5:]
            back = rawDate[0:4]
            combinedDate = front + "-" + back
            self.date_arr.append(combinedDate) 
            dateCell = self.set_date_cell(rawDate)
            venueCell = self.set_venue_cell(date['venue']['displayName'], date['venue']['uri'])
            cityCell = self.set_city_cell(date['location']['city'])
            ticketsCell = self.set_tickets_cell(date['uri'])
            self.showsTableWidget.setItem(row, 0, dateCell)
            self.showsTableWidget.setItem(row, 1, venueCell)
            self.showsTableWidget.setItem(row, 2, cityCell)
            self.showsTableWidget.setItem(row, 3, ticketsCell)
            row += 1

    def set_date_cell(self, date):
        """
        Takes date string and returns a date QTableWidgetItem.
        """
        dateCell = QtWidgets.QTableWidgetItem(date)
        dateCell.setTextAlignment(QtCore.Qt.AlignCenter)
        return dateCell

    def set_venue_cell(self, venue, url):
        """
        Takes venue and venue url strings and returns a venue QTableWidgetItem.
        """
        venueCell = QtWidgets.QTableWidgetItem(venue)
        venueCell.setForeground(QtGui.QBrush(QtGui.QColor(6,69,173)))
        venueCell.setTextAlignment(QtCore.Qt.AlignCenter)
        venueCell.setToolTip(url)
        return venueCell

    def set_city_cell(self, city):
        """
        Takes city string and returns a city QTableWidgetItem.
        """
        cityCell = QtWidgets.QTableWidgetItem(city)
        cityCell.setTextAlignment(QtCore.Qt.AlignCenter)
        return cityCell

    def set_tickets_cell(self, url):
        """
        Takes tickets url string and returns a tickets QTableWidgetItem.
        """
        ticketsCell = QtWidgets.QTableWidgetItem('Tickets')
        ticketsCell.setForeground(QtGui.QBrush(QtGui.QColor(6,69,173)))
        ticketsCell.setTextAlignment(QtCore.Qt.AlignCenter)
        ticketsCell.setToolTip(url)
        return ticketsCell
        
    def date_conversion(self, date_arr):
        """
        Takes a date array containing dates to be converted. Creates a separate thread for multiple
        calls to teammate's microservice so as not to block my GUI.
        https://stackoverflow.com/questions/46781548/updating-variable-values-when-running-a-thread-using-qthread-in-pyqt4
        """
        self.dateThread = DateConversionThread(date_arr)
        self.dateThread.authResult.connect(self.handleDatesResult)
        self.dateThread.start()

    def handleDatesResult(self, result):
        """
        Takes an array containing converted dates and updates display widget.
        https://stackoverflow.com/questions/46781548/updating-variable-values-when-running-a-thread-using-qthread-in-pyqt4
        """
        row = 0
        for newDate in result:
            dateCell = QtWidgets.QTableWidgetItem(newDate)
            dateCell.setTextAlignment(QtCore.Qt.AlignCenter)
            self.showsTableWidget.setItem(row, 0, dateCell)
            row += 1
            self.dateThread.quit()

    def cellHover(self, row, column):
        """
        Event handler for table widget mouse hover.
        """
        item = self.showsTableWidget.item(row, column)
        header = self.showsTableWidget.horizontalHeaderItem(item.column()).text()
        old_item = self.showsTableWidget.item(self.current_hover[0], self.current_hover[1])
        if header == 'VENUE' or header == 'TICKETS':
            if self.current_hover != [row,column]:
                old_item.setBackground(QtGui.QBrush(QtGui.QColor('black')))
                item.setBackground(QtGui.QBrush(QtGui.QColor('yellow')))
            self.current_hover = [row, column]
        else:
            if self.current_hover != [row,column]:
                old_item.setBackground(QtGui.QBrush(QtGui.QColor('black')))
            self.current_hover = [row, column]

#####################################################
#                                                   #
# MAP tab                                           #
#                                                   #
#####################################################

    def searchByCity(self, city):
        """
        Takes a city search string and calls my REST API city-search endpoint, which is a wrapper
        for the Google geolocation API, to find coordinates. Uses coordinates to filter map popups 
        to show only shows in cities a certain distance from searched city. 
        """
        coordinates = self.getCoords(city)
        if not coordinates:
            self.errorBox('Please enter a valid city')
            self.citySearchInput.setText('')
            return
        latCity, lngCity = coordinates
        self.initializeMap((latCity, lngCity), 6)
        distanceFromCity = self.set_distance()
        # filter popups by search radius
        for obj in self.curDates:
            lat = obj['location']['lat']
            lng = obj['location']['lng']
            distance = self.distance(latCity, lat, lngCity, lng)
            if distance < distanceFromCity:
                self.addPopUps(obj)
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())

    def set_distance(self):
        """
        Returns the value selected with the Map tab radio buttons.
        """
        distance = 0
        if self.miles50Radio.isChecked():
            distance = 50
        if self.miles100Radio.isChecked():
            distance = 100
        if self.miles250Radio.isChecked():
            distance = 250
        return distance

    def addPopUps(self, obj):
        """
        Takes a tour date data object and adds popups to the map.
        """
        lat = obj['location']['lat']
        lng = obj['location']['lng']
        # add data to popup dialog in map markers
        iframe = folium.IFrame(f"<section style='font-size: 20px; ' height='80' width='100'><p>{obj['venue']['displayName']}</p><p>{obj['start']['date']}</p><p>{obj['location']['city']}</p></section>")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(
            location=(lat, lng),
            popup=popup,
        ).add_to(self.map)

    def initializeMap(self, coordinates, zoom):
        """
        Takes a set of coordinates as a tuple and a zoom index as an integer and
        draws a Folium map.
        """
        self.map = folium.Map(
            title='',
            zoom_start=zoom,
            location=coordinates
        )
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())

    def clearCity(self):
        """
        Clears current map city focus.
        """
        self.initializeMap((27.03992362079509, -22.920434372492934), 2)
        for obj in self.curDates:
            self.addPopUps(obj)
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())
        self.citySearchInput.setText('')

    def distance(self, lat1, lat2, lon1, lon2):
        """
        Takes two sets of coordinates and computes the distance between the two 
        points using the Haversine formula.
        """
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        # Radius of earth in miles
        r = 3956
        return(c * r)

    def getCoords(self, city):
        """
        Takes a city search string and uses the Google geolocation API to find and return
        the latitude and longitude of the city in a tuple.
        """
        obj = {"city": city}
        response = requests.post('https://showboat-rest-api.herokuapp.com/city-search', data=obj)
        data = response.json()
        return data['coords']

#####################################################
#                                                   #
# VIDEO tab                                         #
#                                                   #
#####################################################

    def video_search(self, artist):
        """
        Takes a search string with the current text in the search bar. Creates a separate thread
        for non-blocking use of an AudioDB web scraper.
        """
        self.videoThread = VideoSearchThread(artist)
        self.videoThread.authResult.connect(self.handleVideoResult)
        self.videoThread.start()

    def handleVideoResult(self, result):
        """
        Takes a JSON object with YouTube urls and updates display widgets.
        """
        if not result:
            for key in self.video_dict:
                self.video_dict[key].setHtml('')
                self.videoSeeMoreButton.setText("See More!")
                self.videoThread.quit()
        else:
            i = 0
            for entry in result:
                if 'channel_url' in entry:
                    self.channelUrl = entry['channel_url']
                else:
                    self.video_dict[f"video{i}"].setHtml(f'<!DOCTYPE html><html><body><iframe width="566" height="320" src="{entry["url"].replace("?v=", "/")}" allowfullscreen></iframe></body></html>', QtCore.QUrl('https://www.youtube.com'))    
                    i += 1
            self.videoSeeMoreButton.setText(f"{self.currentArtist}'s YouTube Channel")
            self.videoThread.quit()
            
    def artistChannelRedirect(self):
        """
        Handles a click on the 'Artist Channel' button for a redirect to their channel in
        a user's browser. Uses global artist channel url variable.
        """
        if self.channelUrl:
            confirm = QtWidgets.QMessageBox()
            confirm.setWindowTitle("Confirm redirect")
            confirm.setText('Link will open in your browser...do you wish to proceed?')
            confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            confirm.exec_()
            if confirm.standardButton(confirm.clickedButton()) == QtWidgets.QMessageBox.Yes:
                self.confirmation = 1
                webbrowser.open(self.channelUrl)
            else:
                self.confirmation = 0

    def video_refresh(self, type):
        """
        Takes a search type as a parameter as chosen by the user via radio buttons and
        refreshes the video display widgets with data by calling the YouTube scraper API
        endpoint.
        """
        obj = {"name": self.currentArtist, "type": type}
        splash_screen = self.loadSplash()
        splash_screen.show()
        app.processEvents()
        response = requests.post('https://youtube-scraper-microservice.herokuapp.com/videos', json=obj)
        data = response.json()
        i = 0
        for entry in data:
            if 'channel_url' in entry:
                continue
            else:
                self.video_dict[f"video{i}"].setHtml(f'<!DOCTYPE html><html><body><iframe width="566" height="320" src="{entry["url"].replace("?v=", "/")}" allowfullscreen></iframe></body></html>', QtCore.QUrl('https://www.youtube.com'))    
                i += 1
        splash_screen.close()
 

# initialize app
app = QtWidgets.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon(LOGO_PATH))
UIWindow = UI()
app.exec_()
