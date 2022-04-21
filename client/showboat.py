from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon, QImage
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import urllib
import pprint

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load UI file
        uic.loadUi("./client/showboat.ui", self)

        # define our widgets

        # Labels
        self.bandPhotoLabel = self.findChild(QtWidgets.QLabel, "bandPhotoLabel")
        self.bandBioHeader = self.findChild(QtWidgets.QLabel, "bandBioHeader")
        self.bandBioLabel = self.findChild(QtWidgets.QLabel, "bandBioLabel")
        self.bandInfoNameLabel = self.findChild(QtWidgets.QLabel, "bandInfoNameLabel")
        self.bandInfoOtherLabel = self.findChild(QtWidgets.QLabel, "bandInfoOtherLabel")
        self.bandInfoWebsiteLabel = self.findChild(QtWidgets.QLabel, "bandInfoWebsiteLabel")
        self.bandBioHeader_2 = self.findChild(QtWidgets.QLabel, "bandBioHeader_2")
        self.tourDatesHomeHeader = self.findChild(QtWidgets.QLabel, "tourDatesHomeHeader")
        self.homeTourDatesLabel = self.findChild(QtWidgets.QLabel, "homeTourDatesLabel")
        # Lists
        
        # Input
        self.bandSearchLineEdit = self.findChild(QtWidgets.QLineEdit, "bandSearchLineEdit")
        # Buttons
        self.lastSearchButton = self.findChild(QtWidgets.QPushButton, "lastSearchButton")
        self.searchButton = self.findChild(QtWidgets.QPushButton, "searchButton")
        # Tabs
        self.homeTab = self.findChild(QtWidgets.QWidget, "homeTab")
        self.tourDatesTab = self.findChild(QtWidgets.QWidget, "tourDatesTab")
        self.mapTab = self.findChild(QtWidgets.QWidget, "mapTab")
        self.videoTab = self.findChild(QtWidgets.QWidget, "videoTab")
        self.infoTab = self.findChild(QtWidgets.QWidget, "infoTab")

        # Functionality

        self.searchButton.clicked.connect(self.add_it)

        # show the app
        self.show()

    # Functions

    def add_it(self):
        response = requests.get('http://127.0.0.1:5000/artist-search')
        data = response.json()
        self.bandInfoNameLabel.setText(data["band"])
        self.bandBioLabel.setText(data["bio"])

        dates = ""
        for date in data["dates"]:
            dates += f"{date['date']}" + " " + f"{date['venue']}" + " " + f"{date['tickets']} \n\n"

        self.homeTourDatesLabel.setText(dates)
        self.bandInfoWebsiteLabel.setText(data["website"])

        img_url = data["image_url"]
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

            
        self.bandSearchLineEdit.setText("")

    def get_photo(self):
        response = requests.get('http://127.0.0.1:5000/band-photo')
        img_url = response.json()["url"]
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

    def artist_search(self):
        search_string = urllib.parse.quote(self.bandSearchLineEdit.text())
        # url = f"https://api.spotify.com/v1/search?q=artist%3A{search_string}&type=artist"
        # headers = {
        #     "Accept": "application/json",
        #     "Content-Type": "application/json",
        #     "Authorization": "Bearer BQD0MtwAM3RNohVy8G61SlaqJt7LfT0L-z7Z2g566kwGXt-YaZoYMPl2w3cqyStytxRhbAF5cKNjHLF3nMni91IzQR0EIh6hgSn30e0xzoVdvF50vDcpeDsKt3jJaF0xDNNq8oYIqCo3rf8"
        # }
        # response = requests.get(url, headers=headers)
        # pprint.pprint(response.json())
        # id = response.json()["artists"]["items"][0]["id"]
        # name = response.json()["artists"]["items"][0]["name"]
        # img_url = response.json()["artists"]["items"][0]["images"][0]["url"]

        bio = self.get_artist_bio(search_string)
        self.load_artist_bio(bio)
        # name = self.get_artist_name(search_string)
        # self.load_photo(img_url)
        # self.load_artist_name(name)

    def load_photo(self, img_url):
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

    def load_artist_name(self, name):
        self.bandInfoNameLabel.setText(name)

    def load_artist_bio(self, bio):
        self.bandBioLabel.setText(bio)

    def get_artist_name(self, search_string):
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={search_string}&api_key={self.API_KEY}&format=json"
        response = requests.get(url)
        name = response.json()
        print("---------------NAME----------------")
        pprint.pprint(name)
        return name

    def get_artist_bio(self, search_string):
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={search_string}&api_key={self.API_KEY}&format=json"
        response = requests.get(url)
        pprint.pprint(response.json())
        bio = response.json()["artist"]["bio"]["summary"]
        print("---------------BIO----------------")
        pprint.pprint(bio)
        return bio

# initialize app
app = QtWidgets.QApplication(sys.argv)
UIWindow = UI()
app.exec_()

