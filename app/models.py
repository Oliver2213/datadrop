# database models for datadrop

import datetime
import pytimeparse
from sqlalchemy import Column, ForeignKey, MetaData, types
from sqlalchemy.orm import relationship
from sqlservice import ModelBase, declarative_base

from app import app
import utils


meta = MetaData()
Model = declarative_base(ModelBase, metadata=meta)

class Drop(Model):
	"""Represents a single "drop" of data, as well as any drop keys it's associated with it."""
	__tablename__ = 'drops'
	id = Column(types.Integer, primary_key=True)
	urlstring = Column(types.String(256), default=utils.random_string(app.config['DATADROP_URLSTRING_LENGTH']), unique=True, nullable=False)
	title = Column(types.String(256))
	# In the future, I might want to split the actual "data" up from the "drops" table, so as to more efficiently store repeated pieces of data
	# but for now:
	data = Column(types.Text(), nullable=False) # text isn't size limited (yet); if it becomes an issue I'll change that
	created_at = Column(types.DateTime, default=datetime.datetime.utcnow(), nullable=False)
	views = Column(types.Integer, default=0)
	publicly_listed = Column(types.Boolean, default=app.config['DATADROP_DEFAULT_LISTED'], nullable=False)
	expires = Column(types.Boolean, default=app.config['DATADROP_DEFAULT_EXPIRES'], nullable=False)
	# expires_ is a time (in a human-friendly format parsed by pytimeparse), after which any drop which is set to expire will be deleted
	# The default is retrieved from the app's config, so **make sure it parses with pytimeparse**
	expires_in = Column(types.Integer, default=pytimeparse.parse(app.config['DATADROP_DEFAULT_EXPIRES_IN']))
	self_destructs = Column(types.Boolean, default=app.config['DATADROP_DEFAULT_SELF_DESTRUCTS'])
	# self_destructs_in is the number of views (which once reached), any drop that is set to self destruct will be deleted
	self_destructs_in = Column(types.Integer, default=app.config['DATADROP_DEFAULT_SELF_DESTRUCTS_IN'])
	drop_keys = relationship('DropKey', secondary='drop_key_associations', back_populates='drops')


class DropKey(Model):
	"""Represents a "drop key", or a unique string of text that associates many "drops" together."""
	__tablename__ = 'drop_keys'
	id = Column(types.Integer, primary_key=True)
	key = Column(types.String(512), nullable=False, unique=True)
	created_at = Column(types.DateTime, default=datetime.datetime.utcnow(), nullable=False)
	drops = relationship('Drop', secondary='drop_key_associations', back_populates='drop_keys')


class DropKeyAssociation(Model):
	__tablename__ = 'drop_key_associations'
	drop_id = Column(types.Integer, ForeignKey('drops.id'), primary_key=True)
	drop_key_id = Column(types.Integer, ForeignKey('drop_keys.id'), primary_key=True)
