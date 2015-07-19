from app.models import User, Item, Transaction, Session
from app.scraping import get_amazon_price


# Cron job for updating db
def cron_update_db():
	session = Session()
	items = session.query(Item).all()

	for item in items:
		url = item.url
		response = get_amazon_price(url)
		price = response.get("price", None)
		
		if price:
			if price < item.price:
				transactions = session.query(Transaction) \
					.filter(Transaction.requested_price > price) \
					.all()

				# send_emails(transactions)
			item.price = price

	session.commit()

cron_update_db()
# def send_emails(transactions):
