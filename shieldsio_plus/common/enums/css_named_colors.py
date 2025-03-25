import json
from pathlib import Path

from shieldsio_plus.common.enums.better_enum import BetterEnum


class _CSSNamedColor(BetterEnum):
	"""
	Enumeration of standard CSS named colors.

	This class provides access to CSS color names
	with their corresponding hex values. The enumeration is dynamically generated
	from a JSON file containing color definitions.
	"""

	@property
	def hex(self) -> str:
		"""
		Gets the hex code for the color.

		Returns:
			str: The hexadecimal color code.
		"""
		return self.value


# Load CSS color definitions from JSON file
with Path("assets/data/css_named_colors.json").resolve().open() as f:
	data = json.load(f)

# Create a list of (color_name, color_value) tuples for enum creation
# Using a dict comprehension with .items() to remove duplicates
data = list({item["slug"].replace("-", "_").upper(): item["hex"] for item in data}.items())

# Dynamically create the CSSNamedColor enum with the processed color data
CSSNamedColor = _CSSNamedColor("CSSNamedColor", data)
