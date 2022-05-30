from datetime import date
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap, QIcon, QImage, QFont, QMovie
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5 import uic
import sys
import os
import io
import folium
import requests
from time import time
import urllib
import pprint
from bs4 import BeautifulSoup
import mechanize
from math import radians, cos, sin, asin, sqrt

# https://github.com/pyinstaller/pyinstaller/issues/1826
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    bundle_dir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
# GUI_PATH = os.path.join( bundle_dir, 'showboat.ui' )
GUI_PATH = os.path.join( bundle_dir, 'showboat.ui' )
IMG_PATH = os.path.join( bundle_dir, 'showboat_white_cropped.png' )

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
        # call video-search endpoint
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
        br.form = list(br.forms())[0]  # use when form is unnamed
        control = br.form.controls[0]
        control.value = self.search_string
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
# Define main window class                                                             #
#                                                                                     #
#######################################################################################

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load UI file
        uic.loadUi(GUI_PATH, self)
        # global 'Previous Search' variable
        self.previousSearch = ''
        self.currentSearch = ''
        # global tab variable
        self.currentTab = 0
        # artist channel url
        self.channelUrl = ''
        # raw date array for conversion
        self.date_arr = []
        self.currentArtist = ''
        self.curDates = []
        self.searchedArtists = "Artists searched:"


#######################################################################################
#                                                                                     #
# Define Widgets                                                                      #
#                                                                                     #
#######################################################################################

        # Initialize status bar
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.setFont(QFont("Tahoma", 16))
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
        self.bandBioHeader = self.findChild(QtWidgets.QLabel, "bandBioHeader")
        self.homeBioPlainTextEdit = self.findChild(QtWidgets.QPlainTextEdit, "homeBioPlainTextEdit")
        self.bandInfoNameLabel = self.findChild(QtWidgets.QLabel, "bandInfoNameLabel")
        self.bandInfoWebsiteLabel = self.findChild(QtWidgets.QLabel, "bandInfoWebsiteLabel")
        self.bandSearchLineEdit = self.findChild(QtWidgets.QLineEdit, "bandSearchLineEdit")
        self.completer = QtWidgets.QCompleter()
        self.bandSearchLineEdit.setCompleter(self.completer)
        self.model = QtCore.QStringListModel()
        self.completer.setModel(self.model)
        self.lastSearchButton = self.findChild(QtWidgets.QPushButton, "lastSearchButton")
        self.searchButton = self.findChild(QtWidgets.QPushButton, "searchButton")

        # Tour Dates

        self.showsTableWidget = self.findChild(QtWidgets.QTableWidget, "showsTableWidget")
        self.artistTourLabel = self.findChild(QtWidgets.QLabel, "artistTourLabel")
        self.showsTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.showsTableWidget.setColumnWidth(0,116)
        self.showsTableWidget.setColumnWidth(1,396)
        self.showsTableWidget.setColumnWidth(2,385)
        self.showsTableWidget.setColumnWidth(3,106)

        # Map
        self.mapMapContainer = self.findChild(QWebEngineView, "mapMapContainer")
        coordinates = (27.03992362079509, -22.920434372492934)
        self.initializeMap(coordinates, 2)
        self.citySearchButton = self.findChild(QtWidgets.QPushButton, "citySearchButton")
        self.clearCityButton = self.findChild(QtWidgets.QPushButton, "clearCityButton")
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

#######################################################################################
#                                                                                     #
# Connect functions to widgets                                                        #
#                                                                                     #
#######################################################################################

        # Functionality
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

        # show the app
        self.show()

#######################################################################################
#                                                                                     #
# Define functions                                                                    #
#                                                                                     #
#######################################################################################

    def populateTourDateCells(self, data):
        """
        """
        row = 0
        self.showsTableWidget.setRowCount(len(data["events"]))
        # loop through events to add cells to table widget
        for date in data["events"]:
            # restructure date for API call to conversion microservice
            rawDate = date['start']['date']
            front = rawDate[5:]
            back = rawDate[0:4]
            combinedDate = front + "-" + back
            self.date_arr.append(combinedDate) 
            # populate tour table widget with data 
            dateCell = QtWidgets.QTableWidgetItem(rawDate)
            dateCell.setTextAlignment(QtCore.Qt.AlignCenter)
            venueCell = QtWidgets.QTableWidgetItem(date['venue']['displayName'])
            venueCell.setTextAlignment(QtCore.Qt.AlignCenter)
            venueCell.setToolTip(date['venue']['uri'])
            cityCell = QtWidgets.QTableWidgetItem(date['location']['city'])
            cityCell.setTextAlignment(QtCore.Qt.AlignCenter)
            ticketsCell = QtWidgets.QTableWidgetItem('Tickets')
            ticketsCell.setTextAlignment(QtCore.Qt.AlignCenter)
            ticketsCell.setToolTip(date['uri'])
            self.showsTableWidget.setItem(row, 0, dateCell)
            self.showsTableWidget.setItem(row, 1, venueCell)
            self.showsTableWidget.setItem(row, 2, cityCell)
            self.showsTableWidget.setItem(row, 3, ticketsCell)
            row += 1

    def addPopUps(self, obj):
        """
        Takes a tour date data object and adds popups to the map.
        """
        lat = obj['location']['lat']
        lng = obj['location']['lng']
        # add data to popup dialog in map markers
        iframe = folium.IFrame(f"<section height='100' width='100'><p>{obj['venue']['displayName']}</p><p>{obj['start']['date']}</p><p>{obj['location']['city']}</p><p><a href='{obj['venue']['uri']} target='_blank'>Tickets</a></p></section>")
        popup = folium.Popup(iframe, min_width=300, max_width=300)
        folium.Marker(
            location=(lat, lng),
            popup=popup,
        ).add_to(self.map)

    def updateWidgets(self, data):
        """
        Takes an artist data object, updates the display widgets, and calls the tour search
        and video search methods..
        """
        self.bandInfoNameLabel.setText(data['artist'])
        self.homeBioPlainTextEdit.clear()
        self.homeBioPlainTextEdit.insertPlainText(data['bio'])
        self.bandInfoWebsiteLabel.setText(f"<a href='www.{data['website']}'>{data['website']}</a>")
        self.set_photo(data['img_url'])
        self.tour_search(data['artist'])
        # creates separate thread for video search microservice calls   
        self.video_search(data['artist'])
        # set prev and cur global search variables
        self.currentArtist = data['artist']
        self.previousSearch = self.currentSearch
        if self.currentArtist not in self.searchedArtists:
            if self.searchedArtists[-1] == ":":  
                self.searchedArtists += f" {data['artist']}"
            else:
                self.searchedArtists += f", {data['artist']}"
        self.currentSearch = data['artist']
        self.statusBar.showMessage(self.searchedArtists)
        self.artistTourLabel.setText(f"{self.currentArtist} tour dates")
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
        splash_screen.setFont(QFont("Britannic Bold", 20))
        splash_screen.showMessage('Loading...', color=QtGui.QColor(200, 47, 101))
        return splash_screen

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
        https://www.geeksforgeeks.org/program-distance-two-points-earth/
        """
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        # Radius of earth in miles
        r = 3956
        # calculate the result
        return(c * r)

    def getCoords(self, city):
        """
        Takes a city search string and uses the Google geolocation API to find and return
        the latitude and longitude of the city in a tuple.
        """
        data = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={os.environ.get('GOOGLE_API_KEY')}")
        if not data.json()['results']:
            return None
        lat = data.json()['results'][0]['geometry']['location']['lat']
        lng = data.json()['results'][0]['geometry']['location']['lng']
        return (lat, lng)

    def searchByCity(self, city):
        """
        Takes a city search string and calls the Google geolocation API to find coordinates.
        Uses coordinates to filter map popups to show only shows in cities a certain distance
        from searched city. 
        """
        coordinates = self.getCoords(city)
        if not coordinates:
            self.errorBox('Please enter a valid city')
            self.citySearchInput.setText('')
            return
        latCity, lngCity = coordinates
        self.initializeMap((latCity, lngCity), 6)
        distanceFromCity = 0
        if self.miles50Radio.isChecked():
            distanceFromCity = 50
        if self.miles100Radio.isChecked():
            distanceFromCity = 100
        if self.miles250Radio.isChecked():
            distanceFromCity = 250
        for obj in self.curDates:
            lat = obj['location']['lat']
            lng = obj['location']['lng']
            distance = self.distance(latCity, lat, lngCity, lng)
            if distance < distanceFromCity:
                self.addPopUps(obj)
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())
            
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

    def keyPressEvent(self, event):
        """
        Handles a 'return' key press by activating the artist search.
        """
        if event.key() == 16777220:
            self.artist_search('key_press')

    def artist_search(self, type):
        """
        Takes a search type (search button clicked or 'return' pressed) and calls the 
        artist search API endpoint. Updates display widgets with returned data.
        """
        # get search string from search bar if search button or 'return' key pressed 
        if type == 'search' or type == 'key_press':
            value = self.bandSearchLineEdit.text()
            # if there's nothing in the search bar
            if not value:
                self.errorBox("Please enter an artist name")
                return
            obj = {"artist_search": value}
        # get global 'previous search' variable if previous button pressed
        else:
            value = self.previousSearch
            # if there hasn't been a search yet
            if not value:
                self.errorBox("Previous search unavailable")
                return
            obj = {"artist_search": value}
        splash_screen = self.loadSplash()
        splash_screen.show()
        app.processEvents()
        # call artist-search endpoint
        response = requests.post('https://showboat-rest-api.herokuapp.com/artist-search', data=obj)
        data = response.json()
        if data['artist']:
            self.updateWidgets(data)
        else:
            self.errorBox("Artist not found")
        # clear search bar    
        self.bandSearchLineEdit.setText("")
        # remove splash screen if content has loaded
        splash_screen.close()

    def video_refresh(self, type):
        """
        Takes a search type as a parameter as chosen by the user via radio buttons and
        refreshes the video display widgets with data by calling the YouTube scraper API
        endpoint.
        """
        obj = {"name": self.bandInfoNameLabel.text(), "type": type}
        splash_screen = self.loadSplash()
        splash_screen.show()
        app.processEvents()
        # call video-search endpoint
        response = requests.post('https://youtube-scraper-microservice.herokuapp.com/videos', json=obj)
        data = response.json()
        i = 0
        for entry in data:
            if 'channel_url' in entry:
                continue
            else:
                self.video_dict[f"video{i}"].setUrl(QtCore.QUrl(entry["url"].replace("embed", "watch")))
                i += 1
        splash_screen.close()

    def tour_search(self, artist):
        """
        Takes an artist name as a parameter and calls the tour search API endpoint which pulls
        Songkick tour data from the web. Also calls teammate's date conversion microservice API
        endpoint. Updates display widgets with returned data.
        """
        self.initializeMap((27.03992362079509, -22.920434372492934), 2)
        # get tour dates
        obj = {"artist_search": artist}
        # call tour-search endpoint
        response = requests.post('https://showboat-rest-api.herokuapp.com/tour-search', data=obj)
        data = response.json()
        # hold dates data for later map manipulation
        self.curDates = data["events"]
        # add dates to map
        for obj in data["events"]:
            self.addPopUps(obj)
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())
        self.populateTourDateCells(data)
        # creates separate thread for date conversion microservice calls     
        self.date_conversion(self.date_arr)

    def auto_complete(self, search_string):
        """
        Takes a search string with the current text in the search bar. Creates a separate thread
        for non-blocking use of an AudioDB web scraper.
        """
        self.autoThread = AutocompleteThread(search_string)
        self.autoThread.authResult.connect(self.handleAutoResult)
        self.autoThread.start()

    def handleAutoResult(self, result):
        """
        Takes result array and updates completer.
        """
        self.model.setStringList(result)
        self.completer.complete()
        self.autoThread.quit()

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
                    self.video_dict[f"video{i}"].setUrl(QtCore.QUrl(entry["url"].replace("embed", "watch")))
                    i += 1
            self.videoSeeMoreButton.setText(f"{self.currentArtist}'s YouTube Channel")
            self.videoThread.quit()

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

# initialize app
QtWidgets.QApplication.setStyle('Fusion')
app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()



