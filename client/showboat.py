import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import uic
import sys
import io
import folium
import requests
import urllib
import pprint

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load UI file
        uic.loadUi("./client/showboat.ui", self)

        # global 'Previous Search' variable
        self.previousSearch = ''
        self.currentSearch = ''

        # define our widgets

        # Tabs
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
        self.lastSearchButton = self.findChild(QtWidgets.QPushButton, "lastSearchButton")
        self.searchButton = self.findChild(QtWidgets.QPushButton, "searchButton")

        # Tour Dates

        self.showsTableWidget = self.findChild(QtWidgets.QTableWidget, "showsTableWidget")
        self.showsTableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.showsTableWidget.setColumnWidth(0,116)
        self.showsTableWidget.setColumnWidth(1,396)
        self.showsTableWidget.setColumnWidth(2,385)
        self.showsTableWidget.setColumnWidth(3,106)

        # Map
        self.mapMapContainer = self.findChild(QWebEngineView, "mapMapContainer")
        coordinates = (27.03992362079509, -22.920434372492934)
        self.map = folium.Map(
            title='',
            zoom_start=2,
            location=coordinates
        )
        # save map data to data object
        data = io.BytesIO()
        self.map.save(data, close_file=False)
        self.mapMapContainer.setHtml(data.getvalue().decode())

        # Video
        self.video0 = self.findChild(QWebEngineView, "video0")
        self.video1 = self.findChild(QWebEngineView, "video1")
        self.video2 = self.findChild(QWebEngineView, "video2")
        # put video widgets in a dict for easy iteration
        self.video_dict = {
            "video0": self.video0,
            "video1": self.video1,
            "video2": self.video2
        }
        self.videoSeeMoreButton = self.findChild(QtWidgets.QPushButton, "videoSeeMoreButton")

        # Functionality
        self.searchButton.clicked.connect(lambda: self.artist_search('search'))
        self.lastSearchButton.clicked.connect(lambda: self.artist_search('previous'))
        self.showsTableWidget.itemDoubleClicked.connect(self.link_clicked)

        # show the app
        self.show()

    # Functions

    def artist_search(self, type):
        # get search string from search bar if search button pressed
        if type == 'search':
            value = self.bandSearchLineEdit.text()
            obj = {"artist_search": value}
        # get global 'previous search' variable if previous button pressed
        else:
            value = self.previousSearch
            # if there hasn't been a search yet
            if not value:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Previous search unavailable")
                x = msg.exec_()
                return
            obj = {"artist_search": value}
        # create and show loading screen
        splash_screen = QtWidgets.QSplashScreen()
        splash_screen.showMessage('Loading...')
        splash_screen.setGeometry(QtCore.QRect(650,400,100,100))
        splash_screen.show()
        app.processEvents()
        # call artist-search endpoint
        response = requests.post('https://showboat-rest-api.herokuapp.com/artist-search', data=obj)
        data = response.json()
        if data['artist']:
            self.bandInfoNameLabel.setText(data['artist'])
            self.homeBioPlainTextEdit.clear()
            self.homeBioPlainTextEdit.insertPlainText(data['bio'])
            self.bandInfoWebsiteLabel.setText(f"<a href='{data['website']}'>{data['website']}</a>")
            self.set_photo(data['img_url'])
            self.tour_search(data['artist'])
            self.video_search(data['id'])
            self.previousSearch = self.currentSearch
            self.currentSearch = data['artist']
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Artist not found")
            x = msg.exec_()
        # clear search bar    
        self.bandSearchLineEdit.setText("")
        # remove splash screen if content has loaded
        splash_screen.close()

    def video_search(self, id):
        obj = {"artist_id": id}
        # call video-search endpoint
        response = requests.post('https://showboat-rest-api.herokuapp.com/video-search', data=obj)
        data = response.json()
        for i, url in enumerate(data["video_urls"]):
            self.video_dict[f"video{i}"].setUrl(QtCore.QUrl(url))

    def tour_search(self, artist):
        # reset map
        coordinates = (27.03992362079509, -22.920434372492934)
        self.map = folium.Map(
            title='',
            zoom_start=2,
            location=coordinates
        )
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())
        # get tour dates
        obj = {"artist_search": artist}
        # call tour-search endpoint
        response = requests.post('https://showboat-rest-api.herokuapp.com/tour-search', data=obj)
        data = response.json()
        # add dates to map
        for obj in data["events"]:
            lat = obj['location']['lat']
            lng = obj['location']['lng']
            # add data to popup dialog in map markers
            iframe = folium.IFrame(f"<section height='100' width='100'><p>{obj['venue']['displayName']}</p><p>{obj['start']['date']}</p><p>{obj['location']['city']}</p><p><a href='{obj['venue']['uri']} target='_blank'>Tickets</a></p></section>")
            popup = folium.Popup(iframe, min_width=300, max_width=300)
            folium.Marker(
                location=(lat, lng),
                popup=popup,
            ).add_to(self.map)
        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())

        row = 0
        self.showsTableWidget.setRowCount(len(data["events"]))

        # loop through events to construct data strings
        for date in data["events"]:
            dateCell = QtWidgets.QTableWidgetItem(date['start']['date'])
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

    def link_clicked(self, item):
        if item.toolTip():
            confirm = QtWidgets.QMessageBox()
            confirm.setWindowTitle("Confirm redirect")
            confirm.setText('Link will open in your browser...do you wish to proceed?')
            confirm.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            confirm.exec_()
            if confirm.standardButton(confirm.clickedButton()) == QtWidgets.QMessageBox.Yes:
                self.confirmation = 1
                # QtGui.QDesktopServices.openUrl(item.text())
                webbrowser.open(item.toolTip())
            else:
                self.confirmation = 0
        
        
    def set_photo(self, img_url):
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

    def confirm_msg(self):
        print("confirm message")

# initialize app
app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()



