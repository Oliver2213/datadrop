# form classes

from wtforms import BooleanField, RadioField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class DropForm(FlaskForm):
	title = StringField('title')
	drop_data = TextAreaField('drop data', validators=[DataRequired("""You need to provide some data for this drop""")])
	publicly_listed = BooleanField('publically listed?')
	submit = SubmitField('save this drop')
