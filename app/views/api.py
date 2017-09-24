# API view functions

from collections import OrderedDict
from flask import jsonify, url_for, redirect, request

from app import app, db, models, utils


@app.route('/api/drop/create', methods=['POST'])
def api_create_drop():
	"""API view function to create a new drop."""
	if request.form.get('data') == None:
		return jsonify({"error": "You must provide some data when creating a new drop."}), 400
	drop = models.Drop()
	title = request.form.get('title')
	if title != None and title != '':
		drop.title = title
	drop.data = request.form.get('data')
	publicly_listed = request.form.get('publicly_listed', app.config['DATADROP_DEFAULT_LISTED'])
	drop.publicly_listed = publicly_listed
	expires = request.form.get('expires', app.config['DATADROP_DEFAULT_EXPIRES'])
	drop.expires = expires
	expires_in = request.form.get('expires_in', app.config['DATADROP_DEFAULT_EXPIRES_IN'])
	drop.expires_in = expires_in
	self_destructs = request.form.get('self_destructs', app.config['DATADROP_DEFAULT_SELF_DESTRUCTS'])
	drop.self_destructs = self_destructs
	drop_key_strings = request.form.getlist('drop_keys')
	if drop_key_strings != None and drop_key_strings != []:
		# for each drop key that was provided, check if it exists in the database;
		# if it doesn't, create it
		drop_keys = [] # a list of key instances
		for k in drop_key_strings:
			potential_key = db.DropKey.filter_by(key=k.lower()).one_or_none()
			if potential_key == None:
				potential_key = db.save(models.DropKey(key=k.lower()))
			drop_keys.append(potential_key)
		drop.drop_keys = drop_keys
	# to avoid unique urlstring errors
	made_urlstring = False
	while made_urlstring == False:
		u = utils.random_string(app.config['DATADROP_URLSTRING_LENGTH'])
		if db.Drop.filter_by(urlstring=u).one_or_none() == None:
			found_urlstring = True
			drop.urlstring = u
	db.save(drop)
	# now build the response
	r = get_drop_dict(drop, include_drop_keys=True)
	return jsonify(r), 201


@app.route('/api/drop/show')
def api_show_drop(include_drop_keys=False):
	"""Return a jsonified response with information about a given response (using an id form parameter)."""
	urlstring = request.data.get('id')
	if urlstring == None:
		return jsonify({"error": "You must provide the ID of a drop to retrieve information for."}), 400
	drop = db.Drop.filter_by(urlstring=urlstring).one_or_none()
	if drop == None:
		return jsonify({"error": "No drop was found with the given ID."})
	else: # drop found
		res = get_drop_dict(drop)
		return jsonify(res)


def get_drop_dict(drop, include_drop_keys=False):
	r = OrderedDict()
	if drop.title:
		r['title'] = drop.title
	r['url'] = url_for('show_drop', urlstring=drop.urlstring, _external=True)
	r['created_at'] = drop.created_at
	r['publicly_listed'] = drop.publicly_listed
	r['expires'] = drop.expires
	if drop.expires:
		r['expires_in'] = drop.expires_in
	r['self_destructs'] = drop.self_destructs
	if include_drop_keys and drop.drop_keys:
		r['drop_keys'] = [k.key for k in drop.drop_keys]
	return r
