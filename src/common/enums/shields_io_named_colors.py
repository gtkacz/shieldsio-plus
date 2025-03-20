from src.common.enums.better_enum import BetterEnum
from src.common.types.hex_code import HexCode


class ShieldsIONamedColors(BetterEnum):
	BRIGHTGREEN = ("brightgreen", HexCode("#4c1"))
	GREEN = ("green", HexCode("#97ca00"))
	YELLOW = ("yellow", HexCode("#dfb317"))
	YELLOWGREEN = ("yellowgreen", HexCode("#a4a61d"))
	ORANGE = ("orange", HexCode("#fe7d37"))
	RED = ("red", HexCode("#e05d44"))
	BLUE = ("blue", HexCode("#007ec6"))
	GREY = ("grey", HexCode("#555"))
	LIGHTGREY = ("lightgrey", HexCode("#9f9f9f"))

	# aliases
	GRAY = GREY
	LIGHTGRAY = LIGHTGREY
	CRITICAL = RED
	IMPORTANT = ORANGE
	SUCCESS = BRIGHTGREEN
	INFORMATIONAL = BLUE
	INACTIVE = LIGHTGREY

	@property
	def slug(self):
		return self.value[0]

	@property
	def hex(self):
		return self.value[1]
