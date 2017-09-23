# utilities

import random
import string


def random_string(length, lowercase=True, uppercase=True):
	"""Return a random string."""
	chars = string.digits
	if lowercase:
		chars += string.lowercase
	if uppercase:
	chars += string.uppercase
	return ''.join(random.choice(chars) for i in range(length))

def get_config_items_with_prefix(config, prefix):
	"""Given a config dictionary and a prefix, return a subset of that config's items that start with prefix."""
	keys = [k for k in config if k.startswith(prefix)]
	r = {}
	for k in keys:
		r[k] = config.get(k)
	return r
