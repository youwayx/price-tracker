from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required, Email

class TrackPriceForm(Form):
	email = TextField('email', validators=[Required(), Email()])
	url = TextField("url", validators=[Required()])
	requested_price = TextField("Requested Price", validators=[Required()])

class ShowTransactionsForm(Form):
	email = TextField('email', validators=[Required(), Email()])