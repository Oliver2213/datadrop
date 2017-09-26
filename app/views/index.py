# index view

import datetime
from flask import flash, render_template, redirect, url_for
import pytimeparse
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
		drop.expires = form.expires
		if form.expires_in.data != None:
			expires_in = pytimeparse.parse(form.expires_in.data)
			if expires_in != None:
				drop.expires_in = expires_in
			else: # the string provided in the post request isn't valid
				drop.expires_in = app.config['DATADROP_DEFAULT_EXPIRES_IN']
				flash("The given expiration time isn't valid; defaulted to {}.".format(app.config['DATADROP_DEFAULT_EXPIRES_IN']))
		drop.self_destructs = form.self_destructs
		if form.self_destructs_in.data != None:
			drop.self_destructs_in = form.self_destructs_in.data
		db.save(drop)
		# now that the drop is in the database (and has a unique urlstring), redirect the user to it's page
		return redirect(url_for('show_drop', urlstring=drop.urlstring))
	else: # form didn't validate; probably a get request
		return render_template('index.html', form=form)
