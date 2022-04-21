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

@app.route("/test")
def tour_dates():
    data = {
        "band": "Radiohead"
    }
    return {
        "band": "Radiohead"
    }

