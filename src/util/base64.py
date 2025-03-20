from base64 import b64decode, b64encode
from pathlib import Path


def svg_to_base64(svg_path: str) -> bytes:
	"""
	Convert a SVG file located in a certain path to a base64 string.

	Args:
		svg_path (str): Path to the SVG file.

	Returns:
		bytes: Base64 string of the SVG file.
	"""
	return b64encode(Path(svg_path).read_bytes())


def is_valid_base_64(data: bytes) -> bool:
	"""
	Check if a string is a valid base64 string.

	Args:
		data (bytes): Base64 string to check.

	Returns:
		bool: True if the base64 string is valid, False otherwise.
	"""
	if not isinstance(data, bytes):
		return False

	try:
		b64decode(data, validate=True)
		return True
	except Exception:
		# If any exception occurs during decoding, the input is not valid base64
		return False
