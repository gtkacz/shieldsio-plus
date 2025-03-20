from dataclasses import dataclass
from operator import itemgetter
from pathlib import Path
from typing import Final, Optional
from urllib.parse import urlencode
from xml.etree import ElementTree as ET

import requests

from src.common.enums import ShieldsIOBadgeStyles, ShieldsIONamedColors
from src.common.types.hex_code import HexColor
from src.common.types.shields_io_color import ShieldsIOColor
from src.util import is_valid_base_64, svg_to_base64


@dataclass
class ShieldsIOBadge:
	slug: str
	label: str
	logo: str
	message: Optional[str] = None
	style: ShieldsIOBadgeStyles = ShieldsIOBadgeStyles.TRUE_FLAT
	color: ShieldsIOColor = ShieldsIONamedColors.BLUE
	label_color: Optional[ShieldsIOColor] = None
	__BASE_URL: Final[str] = "https://img.shields.io/badge/"
	__logo: str = ""
	__color: Optional[str] = None
	__label_color: Optional[str] = None

	def __post_init__(self):
		if self.style not in ShieldsIOBadgeStyles:
			raise ValueError(f"Invalid style: {self.style}")

		self.__logo = svg_to_base64(self.logo)

		if not is_valid_base_64(self.__logo):
			raise ValueError(f"Invalid base64 data: {self.__logo}")

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

	@staticmethod
	def local_name(tag):
		return tag.split("}")[-1] if "}" in tag else tag

	@staticmethod
	def remove_linear_gradients(parent):
		for child in list(parent):
			if ShieldsIOBadge.local_name(child.tag) == "linearGradient":
				parent.remove(child)
			else:
				ShieldsIOBadge.remove_linear_gradients(child)

	@staticmethod
	def remove_shadow_texts(parent):
		"""
		Recursively remove text elements that seem to be used as shadows.
		Here we assume any <text> with aria-hidden="true" or a fill-opacity attribute not equal to "1"
		is a shadow.
		"""
		for child in list(parent):
			if ShieldsIOBadge.local_name(child.tag) == "text":
				if child.attrib.get("aria-hidden") == "true" or (
					child.attrib.get("fill-opacity") and child.attrib.get("fill-opacity") != "1"
				):
					parent.remove(child)
				else:
					ShieldsIOBadge.remove_shadow_texts(child)
			else:
				ShieldsIOBadge.remove_shadow_texts(child)

	@staticmethod
	def parse_real_flat(svg_content: str) -> str:
		root = ET.fromstring(svg_content)

		ShieldsIOBadge.remove_linear_gradients(root)
		ShieldsIOBadge.remove_shadow_texts(root)

		return ET.tostring(root, encoding="unicode")

	def build_base64_logo(self) -> str:
		decoded_data = self.__logo
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
		img_data = requests.get(self.build_shieldsio_url()).content.decode()

		if self.style == ShieldsIOBadgeStyles.TRUE_FLAT:
			img_data = self.parse_real_flat(img_data)

		with open(Path(path + self.style + "/shields", self.slug + ".svg"), "w") as handler:
			handler.write(img_data)

	def to_dict(self) -> dict:
		return {
			"slug": self.slug,
			"label": self.label,
			"message": self.message,
			"style": self.style.value,
			"color": self.__color,
			"label_color": self.__label_color,
			"shields_io_url": self.build_shieldsio_url(),
		}
