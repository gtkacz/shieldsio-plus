from dataclasses import dataclass, field
from operator import itemgetter
from pathlib import Path
from typing import Any, Final, Optional
from urllib.parse import urlencode

from loguru import logger

from src.common.enums.shields_io_badge_styles import ShieldsIOBadgeStyle
from src.common.enums.shields_io_named_colors import ShieldsIONamedColor
from src.common.enums.web_safe_fonts import WebSafeFont
from src.common.types.hex_code import HexColor
from src.common.types.shields_io_color import ShieldsIOColor
from src.common.types.svg import SVG


@dataclass
class ShieldsIOBadge:
	"""
	A class to create and manage Shields.io badges.

	This class handles the creation, styling, and downloading of Shields.io badges
	with customizable properties such as color, style, and logo.

	Attributes:
		slug: A unique identifier for the badge.
		label: The text displayed on the left side of the badge.
		logo: An SVG object representing the badge's logo.
		message: Optional text displayed on the right side of the badge.
		style: The visual style of the badge.
		color: The color for the right side of the badge.
		label_color: Optional color for the left side of the badge.
		logo_color: Optional color for the badge logo.
		font: The font family used for badge text.
	"""

	slug: str
	label: str
	logo: SVG
	message: Optional[str] = None
	style: ShieldsIOBadgeStyle = ShieldsIOBadgeStyle.TRUE_FLAT
	color: ShieldsIOColor = ShieldsIONamedColor.BLUE
	label_color: Optional[ShieldsIOColor] = None
	logo_color: Optional[ShieldsIOColor] = None
	font: WebSafeFont = WebSafeFont.DEFAULT
	__BASE_URL: Final[str] = field(init=False, default="https://img.shields.io/badge/")
	__color: str = field(init=False)
	__label_color: Optional[str] = field(init=False)
	__logo_color: Optional[str] = field(init=False)

	def __post_init__(self) -> None:
		"""
		Initializes internal state after dataclass initialization.

		Validates style and processes color objects into string format.

		Raises:
			ValueError: If the badge style is invalid.
		"""
		# Validate the badge style
		if self.style not in ShieldsIOBadgeStyle:
			raise ValueError(f"Invalid style: {self.style}")

		# Process color objects into string format
		self.__color = self.__parse_shields_io_color_object(self.color)
		self.__label_color = self.__parse_shields_io_color_object(self.label_color)
		self.__logo_color = self.__parse_shields_io_color_object(self.logo_color)

	@staticmethod
	def __parse_shields_io_color_object(color_obj: Optional[ShieldsIOColor]) -> Optional[str]:
		"""
		Converts a ShieldsIOColor object to a string format suitable for Shield.io API.

		Args:
			color_obj: A color object (ShieldsIONamedColor or HexColor) or None.

		Returns:
			The color string without the leading '#' or None if color_obj is None.

		Raises:
			ValueError: If color_obj is not a valid ShieldsIOColor type.
		"""
		if color_obj:
			if isinstance(color_obj, ShieldsIONamedColor):
				return color_obj.slug.removeprefix("#")  # Handle named colors by returning their slug

			if isinstance(color_obj, HexColor):
				return color_obj.hex.removeprefix("#")  # Handle hex colors by returning the hex value

			# Invalid color type
			raise ValueError(f"Invalid color object: {color_obj}")

		return None

	def build_base64_logo(self) -> str:
		"""
		Creates a base64-encoded data URL for the logo.

		Returns:
			A properly formatted data URL containing the base64-encoded SVG logo.
		"""
		decoded_data = self.logo.base64
		return f"data:image/svg%2bxml;base64,{decoded_data}"

	def build_shieldsio_badge_str(self) -> str:
		"""
		Builds the parameter string for the Shields.io API call.

		Creates a formatted string combining badge content and query parameters.

		Returns:
			The formatted badge string for the Shields.io API.
		"""
		badge_content = "-".join(filter(None, [self.label, self.message, self.__color]))

		# Build query parameters
		query = {
			"style": self.style.value,
			"labelColor": self.__label_color,
			"logoColor": self.__logo_color,
			"color": self.__color,
		}

		# Filter out None values from query parameters
		query = dict(filter(itemgetter(1), query.items()))

		# URL encode the query parameters
		query_string = urlencode(query)

		# Combine badge content, query string, and logo
		return f"{badge_content}?{query_string}&logo={self.build_base64_logo()}"

	def build_shieldsio_url(self) -> str:
		"""
		Constructs the complete Shields.io URL for the badge.

		Returns:
			The full URL to retrieve the badge from Shields.io.
		"""
		return self.__BASE_URL + self.build_shieldsio_badge_str()

	def download_shieldsio_badge(self, path: str) -> None:
		"""
		Downloads the badge as an SVG file to the specified path.

		Creates the directory if it doesn't exist, downloads the badge,
		and applies any necessary transformations.

		Args:
			path: The directory path where the badge will be saved.
		"""
		# Create the full path including style subdirectory
		self.path = Path(
			path
			+ "/"
			+ self.style.name.lower()
			+ (f"/{self.font.name.lower()}" if self.font != WebSafeFont.DEFAULT else ""),
		).resolve()

		# Create directories if they don't exist
		if not self.path.exists():
			self.path.mkdir(parents=True, exist_ok=True)

		# Set the file path with slug as filename
		self.path /= f"{self.slug}.svg"

		# Download the SVG data from Shields.io
		img_data = SVG.from_url(self.build_shieldsio_url())

		# Apply TRUE_FLAT or TRUE_FLAT_SQUARE specific transformations
		if self.style.name in {ShieldsIOBadgeStyle.TRUE_FLAT.name, ShieldsIOBadgeStyle.TRUE_FLAT_SQUARE.name}:
			img_data.parse_real_flat()

		# Apply custom font if not using the default
		if self.font != WebSafeFont.DEFAULT:
			img_data.change_font(self.font)

		# Apply custom font if not using the default
		if self.font != WebSafeFont.DEFAULT:
			img_data.change_svg_color(self.font)

		# Write the SVG to file
		img_data.save_to_file(self.path)

		logger.info(f"Downloaded: {self.slug} to {self.path}")

	def to_dict(self) -> dict[str, Any]:
		"""
		Converts the badge object to a dictionary representation.

		Returns:
			A dictionary containing the badge's properties.
		"""
		return {
			"slug": self.slug,
			"label": self.label,
			"message": self.message,
			"style": self.style.name.lower(),
			"color": self.__color,
			"label_color": self.__label_color,
			"logo_color": self.__logo_color,
			"font": self.font.name.lower(),
			"shields_io_url": self.build_shieldsio_url(),
		}
