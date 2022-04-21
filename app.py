
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/artist-search", methods=['GET', 'POST'])
def artist_search():
    
    if request.method == 'POST':    
        data = [{
            "band": "Radiohead",
            "bio": "Radiohead is an excellent band with a weird looking front man.",
            "dates": [{
                "date": "05/04/2022",
                "city": "Seattle",
                "state": "WA",
                "venue": "Doo-doo Arena",
                "tickets": "www.tickets.com"
            },
                {
                "date": "05/06/2022",
                "city": "Phoenix",
                "state": "AZ",
                "venue": "Scrimshaw Center",
                "tickets": "www.getyourtix.com"
            },
                {
                "date": "05/08/2022",
                "city": "Asheville",
                "state": "NC",
                "venue": "Big Outdoor Venue",
                "tickets": "www.tickytickets.com"
            }],
            "website": "www.radiohead.com",
            "image_url": "https://i.guim.co.uk/img/media/c174daa9a205ff9ad68c155bad9003fd946bbf85/0_178_2048_1228/master/2048.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=d0ec33bb206217ddc78f8701fe6a32c4"
        },
        {
            "band": "Kendrick Lamar",
            "bio": "Kendrick Lamar is a great rapper with some certified bangers.",
            "dates": [{
                "date": "06/08/2022",
                "city": "Seattle",
                "state": "WA",
                "venue": "Doo-doo Arena",
                "tickets": "www.tickets.com"
            },
                {
                "date": "06/10/2022",
                "city": "Phoenix",
                "state": "AZ",
                "venue": "Scrimshaw Center",
                "tickets": "www.getyourtix.com"
            },
                {
                "date": "056/12/2022",
                "city": "Asheville",
                "state": "NC",
                "venue": "Big Outdoor Venue",
                "tickets": "www.tickytickets.com"
            }],
            "website": "www.kendricklamar.com",
            "image_url": "https://yt3.ggpht.com/ytc/AKedOLR_U3rEZI1YgAe7YlSAeyr2XOwN1MLfH2G9ZPorDw=s900-c-k-c0x00ffffff-no-rj"
        }]

        for el in data:
            if el["band"] == request.form.get('band_search'):
                return el

@app.route("/city-search", methods=['GET', 'POST'])
def city_search():

    if request.method == 'POST':
        data = [{
            "city": "Portland",
            "state": "OR",
            "coords": (45.52073660670834, -122.66398344934734)
        },
        {
            "city": "Pittsburgh",
            "state": "PA",
            "coords": (40.44011308064731, -79.99509700514174)
        }]

        for el in data:
            if el["city"] == request.form.get('city_search'):
                return el

@app.route("/video-search", methods=['GET', 'POST'])
def video_search():

    if request.method == 'POST':
        data = [{
            "artist": "Radiohead",
            "video_urls": [
                "https://www.youtube.com/watch?v=AOinMjQ9jo8?autoplay=0",
                "https://www.youtube.com/watch?v=lcmbLpCXUGk?autoplay=0",
                "https://www.youtube.com/watch?v=nrxWiU_v9Qs?autoplay=0"
                ]
            },
            {
            "artist": "Kendrick Lamar",
            "video_urls": [
                "https://www.youtube.com/watch?v=JQbjS0_ZfJ0?autoplay=0",
                "https://www.youtube.com/watch?v=K5xERXE7pxI?autoplay=0",
                "https://www.youtube.com/watch?v=GfCqMv--ncA?autoplay=0"
                ]
            },
        ]

        for el in data:
            if el["artist"] == request.form.get('artist'):
                return el