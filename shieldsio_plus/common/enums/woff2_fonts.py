import json
from pathlib import Path
from typing import TypedDict, Union

from shieldsio_plus.common.enums.better_enum import BetterEnum
from shieldsio_plus.common.enums.unicode_ranges import UnicodeRange
from shieldsio_plus.common.types.woff2_font import WOFF2Font


class FontEnumValue(TypedDict):
	"""TypedDict for font enum values."""

	family_name: str
	font_style: str
	font_weight: str
	font_display: str
	src: Union[str, list[str]]
	unicode_range: Union[UnicodeRange, list[UnicodeRange]]


class _KnownWOFF2Fonts(BetterEnum):
	"""Enumeration of known WOFF2 fonts."""

	@property
	def slug(self) -> str:
		return self.name.replace("_", "-").lower()

	@property
	def family_name(self) -> str:
		return self.name

	@property
	def font_style(self) -> str:
		return self.value["font_style"]

	@property
	def font_weight(self) -> str:
		return self.value["font_weight"]

	@property
	def font_display(self) -> str:
		return self.value["font_display"]

	@property
	def src(self) -> Union[str, list[str]]:
		return self.value["src"]

	@property
	def unicode_range(self) -> Union[UnicodeRange, list[UnicodeRange]]:
		return self.value["unicode_range"]


# Load WOFF2 font definitions from JSON file
with Path("assets/data/woff_fonts.json").open(encoding="utf-8") as f:
	data = json.load(f)

parsed_data = []

for dic in data:
	family_name = dic["family-name"]
	font_style = dic["font-style"]
	font_weight = dic["font-weight"]
	font_display = dic["font-display"]
	src = dic["src"]
	unicode_range = dic["unicode-range"]

	if not font_style:
		font_style = "normal"

	if not font_weight:
		font_weight = "400"

	if not font_display:
		font_display = "swap"

	if isinstance(src, list) and (not isinstance(unicode_range, list) or len(src) != len(unicode_range)):
		raise ValueError("src and unicode-range must have the same length if src is a list")

	if not isinstance(unicode_range, list):
		unicode_range = UnicodeRange(unicode_range)

	else:
		unicode_range = [UnicodeRange(range_) for range_ in unicode_range]

# Dynamically create the KnownWOFF2Fonts enum with the processed data
KnownWOFF2Fonts = _KnownWOFF2Fonts("KnownWOFF2Fonts", parsed_data)
