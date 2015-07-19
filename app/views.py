
from scraping import get_amazon_price
from forms import TrackPriceForm
from app import app
import json




@app.route("/track", methods=["POST"])
def track_price():
    form = TrackPriceForm()
    #if form.validate():

    return json.dumps(get_amazon_price(form.url.data))
    #return "wassup"
