# form classes

from wtforms import BooleanField, RadioField, StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

from app import app


class DropForm(FlaskForm):
	title = StringField('title')
	drop_data = TextAreaField('drop data', validators=[DataRequired("""You need to provide some data for this drop""")])
	publicly_listed = BooleanField('publically listed?', default=app.config['DATADROP_DEFAULT_LISTED'])
	expires = BooleanField(label='Expires?', default=app.config['DATADROP_DEFAULT_EXPIRES'], description='Should this drop expire (and delete itself) after a period of time?')
	expires_in = StringField(label='Expires in', default=app.config['DATADROP_DEFAULT_EXPIRES_IN'], description='How long until this drop will expire; example values are 1 day, 2 weeks, 3 weeks 6 hours, 20 mins. This only applies if expires is checked.')
	self_destructs = BooleanField(label='Self destructs?', default=app.config['DATADROP_DEFAULT_SELF_DESTRUCTS'], description='Should this drop delete itself after being viewd a certain number of times?')
	self_destructs_in = IntegerField(label='self destructs in', default=app.config['DATADROP_DEFAULT_SELF_DESTRUCTS_IN'], description='How many times can this drop be retrieved / viewed until it deletes itself? This only applies if self destructs is checked.')
	submit = SubmitField('save this drop')
