from src.common.enums.better_enum import BetterEnum
from src.common.types.hex_code import HexColor


class ShieldsIONamedColors(BetterEnum):
	BRIGHTGREEN = ("brightgreen", HexColor("#4c1"))
	GREEN = ("green", HexColor("#97ca00"))
	YELLOW = ("yellow", HexColor("#dfb317"))
	YELLOWGREEN = ("yellowgreen", HexColor("#a4a61d"))
	ORANGE = ("orange", HexColor("#fe7d37"))
	RED = ("red", HexColor("#e05d44"))
	BLUE = ("blue", HexColor("#007ec6"))
	GREY = ("grey", HexColor("#555"))
	LIGHTGREY = ("lightgrey", HexColor("#9f9f9f"))

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
