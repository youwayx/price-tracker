from app import app
from app.models import User, Item, Transaction, Session
from forms import TrackPriceForm
from scraping import get_amazon_price
import json
from flask import render_template, redirect

@app.route("/")
def hello():
	return "hi"


@app.route("/track", methods=["POST","GET"])
def track_price():
    form = TrackPriceForm()
    if form.validate():
        price_info = get_amazon_price(form.url.data)
        if not price_info.get("success", False):
        	return redirect('/failure')
        else:
            price_info["email"] = form.email.data
            price_info["requested_price"] = form.requested_price.data
            print(price_info)
            response = post_transaction(price_info)
            return redirect('/success')

    return render_template('requestprice.html', form=form)
    	# check if response.get('success') is true
    	# redirect to some success page

def post_transaction(info):
    session = Session()
    email = info['email']
    user_obj = session.query(User).filter(User.email == email).first()
    if not user_obj:
        user_obj = User(email=email)
        session.add(new_user)
        session.commit()

	user_id = user_obj.id

	item_obj = session.query(Item).filter(Item.url == info['url']).first()
	if not item_obj:
		item_obj = Item(url=info['url'], price=info['price'])
		session.add(item_obj)
		session.commit()

	item_id = item_obj.id

	transaction_obj = session.query(Transaction) \
		.filter(Transaction.item_id == item_id) \
		.filter(Transaction.user_id == user_id) \
		.first()

	if transaction_obj:
		transaction_obj.requested_price = info['requested_price']
	else:
		transaction_obj = Transaction(user_id=user_id,
			item_id=item_id,
			requested_price=info['requested_price'])
		session.add(transaction_obj)
	session.commit()

	response = {}
	response['success'] = True
	response['item_id'] = item_id
	response['user_id'] = user_id
	response['requested_price'] = info['requested_price']
	return response
