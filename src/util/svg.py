def read_svg(path: str) -> str:
	"""
	Read the content of a SVG file located in a certain path.

	Args:
		path (str): Path to the SVG file.

	Returns:
		str: Content of the SVG file.
	"""
	with open(path) as handler:
		return handler.read()
