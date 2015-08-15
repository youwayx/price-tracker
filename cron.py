from app.models import User, Item, Transaction, Session
from app.scraping import get_amazon_price
import sendgrid
import os


# Cron job for updating db
def cron_update_db():
	session = Session()
	items = session.query(Item).all()

	for item in items:
		url = item.url
		response = get_amazon_price(url)
		currentPrice = response.get("price", None)

		if currentPrice:
			if currentPrice <= item.price:
				transactions = session.query(Transaction) \
					.filter(Transaction.requested_price >= currentPrice) \
					.all()

				send_emails(transactions)
			item.price = currentPrice


	session.commit()



def send_emails(transactions):
	session = Session()
	for transaction in transactions:
		user = session.query(User) \
			.filter(User.id == transaction.user_id)

		email = user[0].email

		sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_USERNAME'), os.environ.get("SENDGRID_PASSWORD"))
		message = sendgrid.Mail()
		message.add_to(email)
		message.set_from("ioana_crant@hotmail.com")
		message.set_subject("ayyyy lmao")
		message.set_html("yoooooooooooooooo")
		sg.send(message)

cron_update_db()
