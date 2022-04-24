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
        self.map = folium.Map(
            title='',
            zoom_start=3,
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

        self.video_dict = {
            "video0": self.video0,
            "video1": self.video1,
            "video2": self.video2
        }

        self.videoSeeMoreButton = self.findChild(QtWidgets.QPushButton, "videoSeeMoreButton")

        # Functionality

        self.searchButton.clicked.connect(self.artist_search)
        self.mapSetCityButton.clicked.connect(self.city_search_test)

    
        # show the app
        self.show()

    # Functions

    def artist_search(self):
        value = self.bandSearchLineEdit.text()
        obj = {"artist_search": value}
        response = requests.post('http://127.0.0.1:5000/artist-search', data=obj)
        data = response.json()
        pprint.pprint(data)
        self.bandInfoNameLabel.setText(data['artist'])
        self.bandBioLabel.setText(data["bio"])
        self.bandInfoWebsiteLabel.setText(f"<a href='{data['website']}'>{data['website']}</a>")
        
        self.set_photo(data['img_url'])
        self.tour_search(data['artist'])
        self.video_search(data['id'])
            
        # self.bandSearchLineEdit.setText("")

    def video_search(self, id):
        obj = {"artist_id": id}
        response = requests.post('http://127.0.0.1:5000/video-search', data=obj)
        data = response.json()
        pprint.pprint(data)
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
            title=city,
            zoom_start=6,
            location=coords
        )
        data = io.BytesIO()
        map.save(data, close_file=False)
        self.mapMapContainer.setHtml(data.getvalue().decode())

    def tour_search(self, artist):

        obj = {"artist_search": artist}
        response = requests.post('http://127.0.0.1:5000/tour-search', data=obj)
        data = response.json()

        pprint.pprint(data)

        for obj in data["events"]:
            lat = obj['location']['lat']
            lng = obj['location']['lng']
            folium.Marker(
                location=(lat, lng),
                popup=obj['venue']['displayName'],
            ).add_to(self.map)

        map_data = io.BytesIO()
        self.map.save(map_data, close_file=False)
        self.mapMapContainer.setHtml(map_data.getvalue().decode())

        dates = ""
        tourDates = ""
        tourVenues = ""
        tourTickets = ""
        tourCities = ""
        tourStates = ""

        for date in data["events"]:
            dates += f"{date['start']['date']}" + " " + f"{date['venue']['displayName']}" + " " + f"<a href='{date['venue']['uri']}'>{date['venue']['uri']}</a>" + "<br><br>"
            tourDates += f"{date['start']['date']} <br><br>"
            tourVenues += f"{date['venue']['displayName']} <br><br>" 
            tourTickets += f"<a href='{date['venue']['uri']}'>{date['venue']['uri']}</a>" + "<br><br>"
            tourCities += f"{date['location']['city']} <br><br>" 
            # tourStates += f"{date['state']} <br><br>" 

        self.homeTourDatesLabel.setText(dates)
        self.tourDatesDateListLabel.setText(tourDates)
        self.tourDatesVenueListLabel.setText(tourVenues)
        self.tourDatesTicketListLabel.setText(tourTickets)
        # self.tourDatesStateListLabel.setText(tourStates)
        self.tourDatesCityListLabel.setText(tourCities)
        

    def set_photo(self, img_url):
        data = urllib.request.urlopen(img_url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.bandPhotoLabel.setPixmap(pixmap)
        self.bandPhotoLabel.setScaledContents(True)

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

