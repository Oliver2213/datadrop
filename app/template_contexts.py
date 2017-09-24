# module for template context functions

import arrow
from app import app

@app.context_processor
def add_arrow():
	"""This context processor simply adds the arrow module to the global environment for jinja templates."""
	return dict(arrow=arrow)
