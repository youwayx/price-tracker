
import scraping
from forms import TrackPriceForm
from app import app





@app.route("/track", methods=["POST"])
def track_price():
    form = TrackPriceForm()
    if form.validate_on_submit():
        return scraping.get_amazon_price(form.url.data)
