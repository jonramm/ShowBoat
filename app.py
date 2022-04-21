
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/artist-search", methods=['GET', 'POST'])
def tour_dates():
    
    if request.method == 'POST':    
        data = [{
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
        },
        {
            "band": "Kendrick Lamar",
            "bio": "Kendrick Lamar is a great rapper with some certified bangers.",
            "dates": [{
                "date": "06/08/2022",
                "venue": "Doo-doo Arena",
                "tickets": "www.tickets.com"
            },
                {
                "date": "06/10/2022",
                "venue": "Scrimshaw Center",
                "tickets": "www.getyourtix.com"
            },
                {
                "date": "056/12/2022",
                "venue": "Big Outdoor Venue",
                "tickets": "www.tickytickets.com"
            }],
            "website": "www.kendricklamar.com",
            "image_url": "https://yt3.ggpht.com/ytc/AKedOLR_U3rEZI1YgAe7YlSAeyr2XOwN1MLfH2G9ZPorDw=s900-c-k-c0x00ffffff-no-rj"
        }]

        for el in data:
            if el["band"] == request.form.get('band_search'):
                return el

