from dataclasses import dataclass
from operator import itemgetter
from pathlib import Path
from typing import Final, Optional
from urllib.parse import urlencode

import requests

from src.common.enums import ShieldsIOBadgeTypes, ShieldsIONamedColors
from src.common.types.hex_code import HexColor
from src.common.types.shields_io_color import ShieldsIOColor
from src.util import is_valid_base_64


@dataclass
class ShieldsIOBadge:
	slug: str
	label: str
	logo: bytes
	message: Optional[str] = None
	style: ShieldsIOBadgeTypes = ShieldsIOBadgeTypes.FLAT
	color: ShieldsIOColor = ShieldsIONamedColors.BLUE
	label_color: Optional[ShieldsIOColor] = None
	__BASE_URL: Final[str] = "https://img.shields.io/badge/"
	__color: Optional[str] = None
	__label_color: Optional[str] = None

	def __post_init__(self):
		if not is_valid_base_64(self.logo):
			raise ValueError(f"Invalid base64 data: {self.logo}")

		if self.style not in ShieldsIOBadgeTypes:
			raise ValueError(f"Invalid style: {self.style}")

		self.__color = self.__parse_shields_io_color_object(self.color)
		self.__label_color = self.__parse_shields_io_color_object(self.label_color)

	@staticmethod
	def __parse_shields_io_color_object(color_obj: Optional[ShieldsIOColor]) -> str:
		if color_obj:
			if isinstance(color_obj, ShieldsIONamedColors):
				return color_obj.slug.replace("#", "")

			if isinstance(color_obj, HexColor):
				return color_obj.hex.replace("#", "")

			raise ValueError(f"Invalid color object: {color_obj}")

	def build_base64_logo(self) -> str:
		decoded_data = self.logo.decode("utf-8")
		return f"data:image/svg%2bxml;base64,{decoded_data}"

	def build_shieldsio_badge_str(self) -> str:
		badge_content = "-".join(filter(None, [self.label, self.message, self.__color]))

		query = {
			"style": self.style.value,
			"labelColor": self.__label_color,
			"color": self.__color,
		}

		query = dict(filter(itemgetter(1), query.items()))

		query_string = urlencode(query)

		return f"{badge_content}?{query_string}&logo={self.build_base64_logo()}"

	def build_shieldsio_url(self) -> str:
		return self.__BASE_URL + self.build_shieldsio_badge_str()

	def download_shieldsio_badge(self, path: str) -> None:
		img_data = requests.get(self.build_shieldsio_url()).content

		with open(Path(path, self.slug + ".svg"), "wb") as handler:
			handler.write(img_data)

	def to_json(self) -> dict:
		return {
			"slug": self.slug,
			"label": self.label,
			"message": self.message,
			"style": self.style.value,
			"color": self.__color,
			"label_color": self.__label_color,
		}
