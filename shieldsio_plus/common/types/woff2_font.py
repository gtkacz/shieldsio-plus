from base64 import b64decode, b64encode
from binascii import Error as EncodingError
from dataclasses import dataclass, field
from operator import itemgetter

import requests


@dataclass
class WOFF2Font:
	url: str
	b64: str = field(init=False, default="", repr=False)

	def __post_init__(self) -> None:
		"""
		Initialize the object after creation, validate SVG and convert to base64.

		Raises:
			ValueError: If SVG content is empty or base64 conversion fails.
		"""
		if not self.url:
			raise ValueError("SVG content cannot be empty")

		self.woff2_to_base64()

		if not self.is_valid_base_64(self.b64):
			raise ValueError(f"Invalid base64 data: {self.b64}")

	def woff2_to_base64(self) -> None:
		"""
		Convert a WOFF2 font file to base64.

		Raises:
			HTTPError: If the URL is invalid or the request fails.
			ValueError: If the file is not a WOFF2 font.
		"""  # noqa: DOC502
		response = requests.get(self.url)  # noqa: S113
		response.raise_for_status()

		if response.headers["Content-Type"] != "font/woff2":
			raise ValueError("Invalid WOFF2 font file")

		self.b64 = b64encode(response.content).decode()

	@property
	def font_url(self) -> str:
		"""The WOFF2 font URL."""
		return self.url

	@property
	def base64(self) -> str:
		"""The WOFF2 font as base64."""
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

	def build_css_src(self) -> str:
		"""
		Build the CSS `src` value for the WOFF2 font.

		Returns:
			The CSS `src` value.
		"""
		return f"url(data:font/woff2;base64,{self.b64}) format('woff2')"

	def to_css(
		self,
		family_name: str,
		font_style: str = "normal",
		font_weight: str = "400",
		font_display: str = "swap",
		unicode_range: str = "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF",  # noqa: E501
		**kwargs: dict[str, str],
	) -> str:
		"""
		Convert the WOFF2 font to a SVG block.

		Returns:
			The SVG block.
		"""
		params = {
			"font_style": font_style,
			"font_weight": font_weight,
			"font_display": font_display,
			"unicode_range": unicode_range,
			**kwargs,
		}

		params = dict(filter(itemgetter(1), params.items()))

		params_str = " ".join(f"{k.replace("_", "-")}: {v}" for k, v in params.items())
		return f"@font-face {{ font-family: '{family_name}'; {params_str}; src: {self.build_css_src()}; }}"
