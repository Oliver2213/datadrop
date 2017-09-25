# index view

import datetime
from flask import flash, render_template, redirect, url_for
from app import app, db, models
from app.forms import DropForm


@app.route('/', methods=['GET', 'POST'])
def index():
	"""View function for the home page. If there is form data, check it for validity and create a drop from that data if it's valid."""
	form = DropForm()
	if form.validate_on_submit():
		drop = models.Drop()
		if form.title.data != None and form.title.data != '':
			drop.title = form.title.data
		drop.created_at = datetime.datetime.utcnow()
		drop.data = form.drop_data.data
		drop.publicly_listed = form.publicly_listed.data
		# more options will go here once the basics are working
		db.save(drop)
		# now that the drop is in the database (and has a unique urlstring), redirect the user to it's page
		return redirect(url_for('show_drop', urlstring=drop.urlstring))
	else: # form didn't validate; probably a get request
		return render_template('index.html', form=form)
