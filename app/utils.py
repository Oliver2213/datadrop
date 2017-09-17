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
