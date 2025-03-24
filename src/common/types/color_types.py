from typing import NamedTuple


class RGBColor(NamedTuple):
	"""
	Named tuple representing a color in RGB format.

	Attributes:
		r: Red component (0-255)
		g: Green component (0-255)
		b: Blue component (0-255)
	"""

	r: int
	g: int
	b: int


class RGBAColor(NamedTuple):
	"""
	Named tuple representing a color in RGBA format.

	Attributes:
		r: Red component (0-255)
		g: Green component (0-255)
		b: Blue component (0-255)
		a: Alpha/transparency component (0.0-1.0)
	"""

	r: int
	g: int
	b: int
	a: float


class HSLColor(NamedTuple):
	"""
	Named tuple representing a color in HSL format.

	Attributes:
		h: Hue component (0-360 degrees)
		s: Saturation component (0-100 percent)
		l: Lightness component (0-100 percent)
	"""

	h: int
	s: int
	l: int


class HSLAColor(NamedTuple):
	"""
	Named tuple representing a color in HSLA format.

	Attributes:
		h: Hue component (0-360 degrees)
		s: Saturation component (0-100 percent)
		l: Lightness component (0-100 percent)
		a: Alpha/transparency component (0.0-1.0)
	"""

	h: int
	s: int
	l: int
	a: float


class HEXColor(NamedTuple):
	"""
	Named tuple representing a color in hexadecimal format.

	Attributes:
		hex: Hexadecimal color string (e.g., "#RRGGBB" or "#RRGGBBAA")
	"""

	hex: str
