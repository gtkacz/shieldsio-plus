from base64 import b64decode, b64encode


def svg_to_base64(svg_data: str) -> str:
	"""
	Convert a SVG file to a base64 string.

	Args:
		svg_data (str): SVG file to convert.

	Returns:
		str: Base64 string of the SVG file.
	"""
	return b64encode(svg_data.encode()).decode()


def is_valid_base_64(data: str) -> bool:
	"""
	Check if a string is a valid base64 string.

	Args:
		data (str): Base64 string to check.

	Returns:
		bool: True if the base64 string is valid, False otherwise.
	"""
	if not isinstance(data, str):
		return False

	try:
		b64decode(data.encode(), validate=True)
		return True
	except Exception:
		return False
