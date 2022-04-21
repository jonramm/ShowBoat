from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/band-photo")
def band_photo():
    url = "https://i.guim.co.uk/img/media/c174daa9a205ff9ad68c155bad9003fd946bbf85/0_178_2048_1228/master/2048.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=d0ec33bb206217ddc78f8701fe6a32c4"
    return {
        "url": url
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/artist-search")
def tour_dates():
    data = {
        "band": "Radiohead",
        "bio": "Radiohead is an excellent band with a weird looking front man.",
        "dates": [{
            "date": "05/04/2022",
            "venue": "Doo-doo Arena",
            "tickets": "www.tickets.com"
        },
            {
            "date": "05/06/2022",
            "venue": "Scrimshaw Center",
            "tickets": "www.getyourtix.com"
        },
            {
            "date": "05/08/2022",
            "venue": "Big Outdoor Venue",
            "tickets": "www.tickytickets.com"
        }],
        "website": "www.radiohead.com",
        "image_url": "https://i.guim.co.uk/img/media/c174daa9a205ff9ad68c155bad9003fd946bbf85/0_178_2048_1228/master/2048.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=d0ec33bb206217ddc78f8701fe6a32c4"
    }

    return data

