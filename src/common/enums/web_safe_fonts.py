import json
from pathlib import Path
from typing import TypedDict

from src.common.enums.better_enum import BetterEnum


class _WebSafeFontData(TypedDict):
	"""
	Definition of a web-safe font dictionary.

	Each dictionary contains the following
	- family-name: The full name of the font
	- style: The CSS font-family style definition
	"""

	family_name: str
	style: str


class _WebSafeFont(BetterEnum):
	"""
	Enumeration of web-safe fonts for use in web applications.

	This enum provides access to web-safe font definitions with their
	family names, styles, and associated font families.
	"""

	@classmethod
	def get_values_by_key(cls, key: "FontFamily") -> list[dict[str, _WebSafeFontData]]:
		"""
		Returns all font values belonging to a specific font family.

		Args:
			key: The FontFamily enum value to filter by.

		Returns:
			A list of font value dictionaries belonging to the specified family.
		"""
		return [cls(d) for d in cls.values if d["family"] == key]

	@property
	def family_name(self) -> str:
		"""
		Gets the full name of the font.

		Returns:
			The family name of the font (e.g., "Arial", "Times New Roman").
		"""
		return self.value["family-name"]

	@property
	def style(self) -> str:
		"""
		Gets the CSS font-family style definition.

		Returns:
			The CSS font-family string including fallbacks.
		"""
		return self.value["style"]

	@property
	def family(self) -> "FontFamily":
		"""
		Gets the font family enum this font belongs to.

		Returns:
			The FontFamily enum value for this font.
		"""
		return self.value["family"]


class _FontFamily(BetterEnum):
	"""
	Enumeration of font families (sans-serif, serif, monospace, etc.).

	This enum categorizes fonts into their respective families for
	organization and selection.
	"""

	@property
	def fonts(self) -> list["WebSafeFont"]:
		"""
		Gets all fonts belonging to this font family.

		Returns:
			A list of font value dictionaries in this family.
		"""
		return WebSafeFont.get_values_by_key(self)


# Load web safe font definitions from JSON file
with Path("assets/data/web_safe_fonts.json").resolve().open() as f:
	raw_data = json.load(f)

# Create font family enum entries
# Converts keys like "sans-serif" to enum names like "SANS_SERIF"
families_data = list({value.replace("-", "_").upper(): value for value in raw_data}.items())
FontFamily = _FontFamily("FontFamily", families_data)

# Create web safe font enum entries
# Process each font definition and add to enum
fonts_data = [
	*list(
		{
			d["family-name"].replace(" ", "_").upper(): d
			| {"family": FontFamily(d["style"].split(",")[-1].split(";")[0])}
			for d in [item for sublist in raw_data.values() for item in sublist]
		}.items(),
	),
	(
		"DEFAULT",
		{
			"family-name": "Default",
			"style": "Verdana,Geneva,DejaVu Sans,sans-serif !important",
			"family": FontFamily.SANS_SERIF,
		},
	),
]

# Create the WebSafeFont enum with the processed font data
WebSafeFont = _WebSafeFont("WebSafeFont", fonts_data)
