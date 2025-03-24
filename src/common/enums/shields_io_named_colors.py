from src.common.enums.better_enum import BetterEnum
from src.common.types.hex_code import HexColor


class ShieldsIONamedColor(BetterEnum):
	"""
	Enumeration of predefined named colors supported by Shields.io.

	This enum provides access to the standard color palette offered by Shields.io,
	with both the API slug and corresponding hex color value for each color.

	Elements:
		BRIGHTGREEN: Bright green color (#4c1)
		GREEN: Standard green color (#97ca00)
		YELLOW: Yellow color (#dfb317)
		YELLOWGREEN: Yellow-green color (#a4a61d)
		ORANGE: Orange color (#fe7d37)
		RED: Red color (#e05d44)
		BLUE: Blue color (#007ec6)
		GREY: Grey color (#555)
		LIGHTGREY: Light grey color (#9f9f9f)

		Aliases:
		GRAY: Alias for GREY
		LIGHTGRAY: Alias for LIGHTGREY
		CRITICAL: Alias for RED
		IMPORTANT: Alias for ORANGE
		SUCCESS: Alias for BRIGHTGREEN
		INFORMATIONAL: Alias for BLUE
		INACTIVE: Alias for LIGHTGREY
	"""

	BRIGHTGREEN = ("brightgreen", HexColor("#4c1"))
	GREEN = ("green", HexColor("#97ca00"))
	YELLOW = ("yellow", HexColor("#dfb317"))
	YELLOWGREEN = ("yellowgreen", HexColor("#a4a61d"))
	ORANGE = ("orange", HexColor("#fe7d37"))
	RED = ("red", HexColor("#e05d44"))
	BLUE = ("blue", HexColor("#007ec6"))
	GREY = ("grey", HexColor("#555"))
	LIGHTGREY = ("lightgrey", HexColor("#9f9f9f"))

	# Aliases for convenience and semantic naming
	GRAY = GREY
	LIGHTGRAY = LIGHTGREY
	CRITICAL = RED
	IMPORTANT = ORANGE
	SUCCESS = BRIGHTGREEN
	INFORMATIONAL = BLUE
	INACTIVE = LIGHTGREY

	@property
	def slug(self) -> str:
		"""
		Gets the slug identifier for the color.

		Returns:
			str: The Shields.io API slug for this color.
		"""
		return self.value[0]

	@property
	def hex(self) -> str:
		"""
		Gets the hexadecimal color code.

		Returns:
			str: The hex color code as a string.
		"""
		return self.value[1].hex
