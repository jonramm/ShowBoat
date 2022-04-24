import os
from flask import Flask, request, jsonify
import requests
import pprint

app = Flask(__name__)

@app.route("/artist-search", methods=['GET', 'POST'])
def artist_search():
    if request.method == 'POST':
        url = f"https://www.theaudiodb.com/api/v1/json/2/search.php?s={request.form.get('artist_search')}"
        response = requests.get(url)
        data = response.json()
        if data['artists']:
            obj = {
                'artist': data['artists'][0]['strArtist'],
                'bio': data['artists'][0]['strBiographyEN'],
                'img_url': data['artists'][0]['strArtistThumb'],
                'website': data['artists'][0]['strWebsite'],
                'id': data['artists'][0]['idArtist']
            }
        else:
            obj = {
                'artist': None
            }
        return obj


@app.route("/tour-search", methods=['GET', 'POST'])
def tour_search():
    if request.method == 'POST':
        id_url = f"https://api.songkick.com/api/3.0/search/artists.json?apikey={os.getenv('SONGKICK_API_KEY')}&query={request.form.get('artist_search')}"
        response = requests.get(id_url)
        id_data = response.json()

        id = id_data['resultsPage']['results']['artist'][0]['id']

        tour_url = f"https://api.songkick.com/api/3.0/artists/{id}/calendar.json?apikey={os.getenv('SONGKICK_API_KEY')}"
        response = requests.get(tour_url)
        tour_data = response.json()

        if tour_data['resultsPage']['results']:
            events = tour_data['resultsPage']['results']['event']
        else:
            events = []

        obj = {
            'events': events
        }

        return obj
        

@app.route("/video-search", methods=['GET', 'POST'])
def video_search():

    if request.method == 'POST':
        url = f"https://theaudiodb.com/api/v1/json/2/mvid.php?i={request.form.get('artist_id')}"
        response = requests.get(url)
        data = response.json()
        video_urls = []
        if data['mvids']:
            numVids = len(data['mvids'])
            if numVids < 3:
                indexes = numVids
            else:
                indexes = 3
        else:
            indexes = 0
        for i in range(indexes):
            if data['mvids']:
                video_urls.append(data['mvids'][i]['strMusicVid'])
        obj = {
            'video_urls': video_urls
        }
        return obj

