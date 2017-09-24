# drop-related views

from flask import render_template, render_template_string, flash, Response
from app import app, db, models


@app.route('/drop/<urlstring>')
def show_drop(urlstring):
	"""Return a page containing the given drop (if the given urlstring exists)."""
	drop = db.Drop.filter_by(urlstring=urlstring).one_or_none()
	if drop != None: # a drop with the provided urlstring exists
		return render_template('drop.html', drop=drop)
	else: # no drop
		return render_template('drop_not_found.html'), 404

@app.route('/raw/<urlstring>')
def show_raw_drop(urlstring):
	"""Return the drop with the given urlstring (if it exists); this is different from show_drop because it doesn't put the normal datadrop web things around it (headings, navigation, etc)."""
	drop = db.Drop.filter_by(urlstring=urlstring).one_or_none()
	if drop != None:
		# explicitly create the response object here, because the mimetype needs to be text/plain
		resp = Response(drop.data, mimetype='text/plain')
		return resp
	else:
		return render_template('drop_not_found'), 404
