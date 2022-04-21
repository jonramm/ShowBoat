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
        self.bandBioLabel = self.findChild(QtWidgets.QLabel, "bandBioLabel")
        self.bandInfoNameLabel = self.findChild(QtWidgets.QLabel, "bandInfoNameLabel")
        self.bandInfoWebsiteLabel = self.findChild(QtWidgets.QLabel, "bandInfoWebsiteLabel")
        self.bandBioHeader_2 = self.findChild(QtWidgets.QLabel, "bandBioHeader_2")
        self.tourDatesHomeHeader = self.findChild(QtWidgets.QLabel, "tourDatesHomeHeader")
        self.homeTourDatesLabel = self.findChild(QtWidgets.QLabel, "homeTourDatesLabel")
        
        self.bandSearchLineEdit = self.findChild(QtWidgets.QLineEdit, "bandSearchLineEdit")

        self.lastSearchButton = self.findChild(QtWidgets.QPushButton, "lastSearchButton")
        self.searchButton = self.findChild(QtWidgets.QPushButton, "searchButton")

        # Tour Dates
        self.tourDatesDateLabel = self.findChild(QtWidgets.QLabel, "tourDatesDateLabel")
        self.tourDatesVenueLabel = self.findChild(QtWidgets.QLabel, "tourDatesVenueLabel")
        self.tourDatesCityLabel = self.findChild(QtWidgets.QLabel, "tourDatesCityLabel")
        self.tourDatesStateLabel = self.findChild(QtWidgets.QLabel, "tourDatesStateLabel")
        self.tourDatesTicketInfoLabel = self.findChild(QtWidgets.QLabel, "tourDatesTicketInfoLabel")
        self.tourDatesDateListLabel = self.findChild(QtWidgets.QLabel, "tourDatesDateListLabel")
        self.tourDatesVenueListLabel = self.findChild(QtWidgets.QLabel, "tourDatesVenueListLabel")
        self.tourDatesCityListLabel = self.findChild(QtWidgets.QLabel, "tourDatesCityListLabel")
        self.tourDatesStateListLabel = self.findChild(QtWidgets.QLabel, "tourDatesStateListLabel")
        self.tourDatesTicketListLabel = self.findChild(QtWidgets.QLabel, "tourDatesTicketListLabel")

        # Map
        self.mapMapContainer = self.findChild(QWebEngineView, "mapMapContainer")
        self.mapHomeCityLineEdit = self.findChild(QtWidgets.QLineEdit, "mapHomeCityLineEdit")
        self.mapSetRadiusSlider = self.findChild(QtWidgets.QSlider, "mapSetRadiusSlider")
        self.mapSetCityButton = self.findChild(QtWidgets.QPushButton, "mapSetCityButton")
        self.mapDateDisplayLabel = self.findChild(QtWidgets.QLabel, "mapDateDisplayLabel")
        self.mapVenueDisplayLabel = self.findChild(QtWidgets.QLabel, "mapVenueDisplayLabel")
        self.mapCityDisplayLabel = self.findChild(QtWidgets.QLabel, "mapCityDisplayLabel")
        self.mapTicketsDisplayLabel = self.findChild(QtWidgets.QLabel, "mapTicketsDisplayLabel")

        coordinates = (39.70495909177235, -101.79370097549975)
        map = folium.Map(
            title='Santa Fe',
            zoom_start=3,
            location=coordinates
        )

        # save map data to data object
        data = io.BytesIO()
        map.save(data, close_file=False)

        self.mapMapContainer.setHtml(data.getvalue().decode())

        # Video

        self.video0 = self.findChild(QWebEngineView, "video0")
        self.video1 = self.findChild(QWebEngineView, "video1")
        self.video2 = self.findChild(QWebEngineView, "video2")

        self.video_dict = {
            "video0": self.video0,
            "video1": self.video1,
            "video2": self.video2
        }

        # url = "https://www.youtube.com/watch?v=JQbjS0_ZfJ0?autoplay=0"
        # self.video_dict["video0"].setUrl(QtCore.QUrl(url))

        self.videoSeeMoreButton = self.findChild(QtWidgets.QPushButton, "videoSeeMoreButton")

        # Functionality

        self.searchButton.clicked.connect(self.artist_search_test)
        self.mapSetCityButton.clicked.connect(self.city_search_test)

        

        # show the app
        self.show()

    # Functions

    def video_search_test(self, artist):
        obj = {"artist": artist}
        response = requests.post('http://127.0.0.1:5000/video-search', data=obj)
        data = response.json()

        for i, url in enumerate(data["video_urls"]):
            self.video_dict[f"video{i}"].setUrl(QtCore.QUrl(url))

    def city_search_test(self):
        value = self.mapHomeCityLineEdit.text()
        obj = {"city_search": value}
        response = requests.post('http://127.0.0.1:5000/city-search', data=obj)
        data = response.json()
        city = data["city"] + ", " + data["state"]
        coords = data["coords"]

        map = folium.Map(
            title='Santa Fe',
            zoom_start=6,
            location=coords
        )
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.mapMapContainer.setHtml(data.getvalue().decode())


    def artist_search_test(self):
        value = self.bandSearchLineEdit.text()
        obj = {"band_search": value}
        response = requests.post('http://127.0.0.1:5000/artist-search', data=obj)
        data = response.json()
        self.bandInfoNameLabel.setText(data["band"])
        self.bandBioLabel.setText(data["bio"])

        dates = ""
        tourDates = ""
        tourVenues = ""
        tourTickets = ""
        tourCities = ""
        tourStates = ""

        for date in data["dates"]:
            dates += f"{date['date']}" + " " + f"{date['venue']}" + " " + f"<a href='{date['tickets']}'>{date['tickets']}</a>" + "<br><br>"
            tourDates += f"{date['date']} <br><br>"
            tourVenues += f"{date['venue']} <br><br>" 
            tourTickets += f"<a href='{date['tickets']}'>{date['tickets']}</a> <br><br>"
            tourCities += f"{date['city']} <br><br>" 
            tourStates += f"{date['state']} <br><br>" 

        self.homeTourDatesLabel.setText(dates)
        self.tourDatesDateListLabel.setText(tourDates)
        self.tourDatesVenueListLabel.setText(tourVenues)
        self.tourDatesTicketListLabel.setText(tourTickets)
        self.tourDatesStateListLabel.setText(tourStates)
        self.tourDatesCityListLabel.setText(tourCities)
        self.bandInfoWebsiteLabel.setText(f"<a href='{data['website']}'>{data['website']}</a>")

        img_url = data["image_url"]
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

        self.video_search_test(value)
            
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

