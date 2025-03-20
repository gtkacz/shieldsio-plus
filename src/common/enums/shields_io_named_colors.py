from typing import Tuple

from src.common.enums.better_enum import BetterEnum
from src.common.types.hex_code import HexCode

ShieldsIONamedColorsValue = Tuple[str, HexCode]

class ShieldsIONamedColors(BetterEnum):
	BRIGHTGREEN: ShieldsIONamedColorsValue = ("brightgreen", HexCode("#4c1"))
	GREEN: ShieldsIONamedColorsValue = ("green", HexCode("#97ca00"))
	YELLOW: ShieldsIONamedColorsValue = ("yellow", HexCode("#dfb317"))
	YELLOWGREEN: ShieldsIONamedColorsValue = ("yellowgreen", HexCode("#a4a61d"))
	ORANGE: ShieldsIONamedColorsValue = ("orange", HexCode("#fe7d37"))
	RED: ShieldsIONamedColorsValue = ("red", HexCode("#e05d44"))
	BLUE: ShieldsIONamedColorsValue = ("blue", HexCode("#007ec6"))
	GREY: ShieldsIONamedColorsValue = ("grey", HexCode("#555"))
	LIGHTGREY: ShieldsIONamedColorsValue = ("lightgrey", HexCode("#9f9f9f"))

	# aliases
	GRAY = GREY
	LIGHTGRAY = LIGHTGREY
	CRITICAL = RED
	IMPORTANT = ORANGE
	SUCCESS = BRIGHTGREEN
	INFORMATIONAL = BLUE
	INACTIVE = LIGHTGREY

	@property
	def slug(self) -> str:
		return self.value[0]

	@property
	def hex(self) -> str:
		return self.value[1].hex
