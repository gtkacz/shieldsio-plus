from base64 import b64decode, b64encode
from binascii import Error as EncodingError
from dataclasses import dataclass, field
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from src.common.enums.web_safe_fonts import WebSafeFont


@dataclass
class SVG:
	"""
	Class for handling SVG files, including conversion to base64, validation, and modifications.

	This class allows loading SVGs from files or URLs, converting them to base64 format,
	and applying various transformations to the SVG content.

	Attributes:
		svg_str: The SVG content as a string
		b64: Base64 encoded representation of the SVG (auto-generated)
	"""

	svg_str: str
	b64: str = field(init=False, default="")

	def __post_init__(self) -> None:
		"""
		Initialize the object after creation, validate SVG and convert to base64.

		Raises:
			ValueError: If SVG content is empty or base64 conversion fails.
		"""
		if not self.svg_str:
			raise ValueError("SVG content cannot be empty")

		self.svg_to_base64()

		if not self.is_valid_base_64(self.b64):
			raise ValueError(f"Invalid base64 data: {self.b64}")

	@classmethod
	def from_file(cls, path: str) -> "SVG":
		"""
		Create an SVG object from a file.

		Args:
			path: Path to the SVG file.

		Returns:
			A new SVG object with content from the file.
		"""
		with Path(path).resolve().open() as handler:
			return cls(handler.read())

	@classmethod
	def from_url(cls, url: str) -> "SVG":
		"""
		Create an SVG object by downloading from a URL.

		Args:
			url: URL to the SVG resource.

		Returns:
			A new SVG object with content from the URL.
		"""
		return cls(requests.get(url).content.decode())  # noqa: S113

	def svg_to_base64(self) -> None:
		"""
		Convert the SVG string to base64 encoding.

		Updates the b64 attribute with the base64 encoded version of the SVG.
		"""
		self.b64 = b64encode(self.svg_str.encode()).decode()

	@property
	def svg(self) -> str:
		"""
		Get the SVG content as a string.

		Returns:
			The SVG content.
		"""
		return self.svg_str

	@property
	def base64(self) -> str:
		"""
		Get the base64 encoded SVG.

		Returns:
			The base64 encoded SVG string.
		"""
		return self.b64

	@staticmethod
	def is_valid_base_64(data: str) -> bool:
		"""
		Check if a string is valid base64 encoding.

		Args:
			data: String to check.

		Returns:
			True if the string is valid base64, False otherwise.
		"""
		if not isinstance(data, str):
			return False

		try:
			b64decode(data.encode(), validate=True)
			return True
		except EncodingError:
			return False
		else:
			return False

	@staticmethod
	def local_name(tag: str) -> str:
		"""
		Extract the local name from an XML tag, removing any namespace.

		Args:
			tag: XML tag possibly with namespace.

		Returns:
			The tag without namespace.
		"""
		return tag.split("}")[-1] if "}" in tag else tag

	@staticmethod
	def remove_linear_gradients(parent: BeautifulSoup) -> None:
		"""
		Recursively remove all linearGradient elements from a BeautifulSoup object.

		Args:
			parent: Parent BeautifulSoup object to process.
		"""
		linear_gradients = parent.find_all(lambda tag: SVG.local_name(tag.name) == "linearGradient")
		for gradient in linear_gradients:
			gradient.decompose()

	@staticmethod
	def remove_shadow_texts(parent: BeautifulSoup) -> None:
		"""
		Recursively remove text elements that appear to be shadows.

		Removes text elements with aria-hidden="true" or fill-opacity
		attribute not equal to "1".

		Args:
			parent: Parent BeautifulSoup object to process.
		"""
		shadow_texts = parent.find_all(
			lambda tag: SVG.local_name(tag.name) == "text"
			and (tag.get("aria-hidden") == "true" or (tag.get("fill-opacity") and tag.get("fill-opacity") != "1")),
		)
		for text in shadow_texts:
			text.decompose()

	def parse_real_flat(self) -> None:
		"""
		Transform the SVG to a flat style by removing gradients and shadow texts.

		This method parses the SVG, removes linearGradient elements and shadow texts,
		and updates the svg_str attribute.

		Raises:
			ValueError: If the SVG content cannot be parsed.
		"""
		try:
			soup = BeautifulSoup(self.svg_str, "xml")
		except Exception as e:
			raise ValueError(f"Invalid SVG content: {self.svg_str}") from e

		self.remove_linear_gradients(soup)
		self.remove_shadow_texts(soup)

		self.svg_str = str(soup)
		self.svg_to_base64()  # Update base64 after modifying SVG

	def change_svg_color(self, color: str) -> None:
		"""
		Change the color of path elements in the SVG.

		Args:
			color: New color value to apply (CSS color format).

		Raises:
			ValueError: If the SVG content cannot be parsed.
		"""
		try:
			soup = BeautifulSoup(self.svg_str, "xml")
		except Exception as e:
			raise ValueError(f"Invalid SVG content: {self.svg_str}") from e

		for path in soup.find_all(lambda tag: SVG.local_name(tag.name) == "path" and tag.has_attr("fill")):
			path["fill"] = color

		self.svg_str = str(soup)
		self.svg_to_base64()  # Update base64 after modifying SVG

	def change_font(self, font: WebSafeFont) -> None:
		"""
		Change the font of text elements in the SVG.

		Args:
			font: Font object with style attribute to apply.

		Raises:
			ValueError: If the SVG content cannot be parsed.
		"""
		try:
			soup = BeautifulSoup(self.svg_str, "xml")
		except Exception as e:
			raise ValueError(f"Invalid SVG content: {self.svg_str}") from e

		for text in soup.find_all(lambda tag: SVG.local_name(tag.name) in {"text", "g"}):
			text["font-family"] = font.style.removeprefix("font-family: ").removesuffix("; !important").replace('"', "")

		self.svg_str = str(soup)
		self.svg_to_base64()  # Update base64 after modifying SVG

	def save_to_file(self, path: str) -> None:
		"""
		Save the SVG content to a file.

		Args:
			path: Path to save the SVG content to.
		"""
		with Path(path).resolve().open("w") as handler:
			handler.write(self.svg_str)
