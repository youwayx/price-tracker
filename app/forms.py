from flask.ext.wtf import Form
from wtforms.fields import TextField, DecimalField
from wtforms.validators import Required, Email

class TrackPriceForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    url = TextField("URL", validators=[Required()])
    requestedprice = DecimalField("Requested Price", validators=[Required()])
