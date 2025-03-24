from dataclasses import dataclass

from scipy.spatial.distance import euclidean

from shieldsio_plus.common.enums.css_named_colors import CSSNamedColor
from shieldsio_plus.common.types.color_types import HSLAColor, HSLColor, RGBAColor, RGBColor
from shieldsio_plus.util import is_valid_hex_code


@dataclass(frozen=True)
class HexColor:
	"""
	A class representing a color in hexadecimal format.

	This class provides methods to convert between hex color codes and other
	color formats such as RGB, RGBA, HSL, and HSLA.

	Attributes:
		value: The hexadecimal color code without the leading '#'.
	"""

	value: str

	def __init__(self, value: str) -> None:
		"""
		Initialize a HexColor object.

		Args:
			value: A string representing a hexadecimal color code.
				Can include a leading '#' which will be removed.

		Raises:
			ValueError: If the provided value is not a valid hexadecimal color code.
		"""
		processed_value = value if not value.startswith("#") else value[1:]
		object.__setattr__(self, "value", processed_value)

		if not is_valid_hex_code(self.value):
			raise ValueError(f"Invalid hex code: {self.value}")

	def __str__(self) -> str:  # noqa: D105
		return self.hex

	@property
	def hex(self) -> str:
		"""
		Get the hex color code with the leading '#'.

		Returns:
			A string representing the hex color code with the leading '#'.
		"""
		return "#" + self.value

	@property
	def rgb(self) -> RGBColor:
		"""
		Get the RGB representation of the color.

		Returns:
			A tuple of three integers representing the red, green, and blue components.
		"""
		return self.to_rgb()

	@property
	def rgba(self) -> RGBAColor:
		"""
		Get the RGBA representation of the color.

		Returns:
			A tuple of three integers and a float representing the red, green, blue,
			and alpha components.
		"""
		return self.to_rgba()

	@property
	def hsl(self) -> HSLColor:
		"""
		Get the HSL representation of the color.

		Returns:
			A tuple of three integers representing the hue, saturation, and lightness
			components.
		"""
		return self.to_hsl()

	@property
	def hsla(self) -> HSLAColor:
		"""
		Get the HSLA representation of the color.

		Returns:
			A tuple of three integers and a float representing the hue, saturation,
			lightness, and alpha components.
		"""
		return self.to_hsla()

	@property
	def css(self) -> str:
		"""
		Get the CSS representation of the color.

		Returns:
			A string representing the CSS color value.
		"""
		return self.to_css()

	def to_rgb(self) -> RGBColor:
		"""
		Convert the hex color code to RGB format.

		Returns:
			A tuple of three integers representing the red, green, and blue components.
		"""
		hex_value = self.value

		if len(hex_value) == 3:  # Handle shorthand hex (e.g., "fff" to "ffffff")
			hex_value = "".join(c + c for c in hex_value)

		r = int(hex_value[0:2], 16)
		g = int(hex_value[2:4], 16)
		b = int(hex_value[4:6], 16)

		return (r, g, b)

	@classmethod
	def from_rgb(cls, rgb: RGBColor) -> "HexColor":
		"""
		Create a HexColor object from RGB values.

		Args:
			rgb: A tuple of three integers representing the red, green, and blue components.
				Each component should be in the range [0, 255].

		Returns:
			A new HexColor object.

		Raises:
			ValueError: If any RGB component is outside the valid range.
		"""
		r, g, b = rgb

		# Validate RGB values
		if not all(0 <= c <= 255 for c in rgb):
			raise ValueError(f"Invalid RGB values: {rgb}. Values must be between 0 and 255.")

		hex_value = f"{r:02x}{g:02x}{b:02x}"
		return cls(hex_value)

	def to_rgba(self) -> RGBAColor:
		"""
		Convert the hex color code to RGBA format.

		Returns:
			A tuple of three integers and a float representing the red, green, blue,
			and alpha components. Alpha will be 1.0 if not specified in the hex code.
		"""
		hex_value = self.value

		if len(hex_value) == 3:  # Handle shorthand hex (e.g., "fff" to "ffffff")
			hex_value += hex_value

		r = int(hex_value[0:2], 16)
		g = int(hex_value[2:4], 16)
		b = int(hex_value[4:6], 16)

		# Check if alpha channel is present
		a = int(hex_value[6:8], 16) / 255 if len(hex_value) == 8 else 1.0

		return (r, g, b, a)

	@classmethod
	def from_rgba(cls, rgba: RGBAColor) -> "HexColor":
		"""
		Create a HexColor object from RGBA values.

		Args:
			rgba: A tuple of three integers and a float representing the red, green, blue,
				and alpha components. RGB values should be in the range [0, 255],
				and alpha should be in the range [0, 1].

		Returns:
			A new HexColor object.

		Raises:
			ValueError: If any component is outside the valid range.
		"""
		r, g, b, a = rgba

		# Validate RGBA values
		if not all(0 <= c <= 255 for c in (r, g, b)):
			raise ValueError(f"Invalid RGB values in {rgba}. RGB values must be between 0 and 255.")

		if not 0 <= a <= 1:
			raise ValueError(f"Invalid alpha value in {rgba}. Alpha must be between 0 and 1.")

		# Convert alpha to hex
		alpha_hex = f"{int(a * 255):02x}"

		hex_value = f"{r:02x}{g:02x}{b:02x}{alpha_hex}"
		return cls(hex_value)

	def to_hsl(self) -> HSLColor:
		"""
		Convert the hex color code to HSL format.

		Returns:
			A tuple of three integers representing the hue (0-360), saturation (0-100),
			and lightness (0-100) components.
		"""
		r, g, b = self.to_rgb()

		# Convert RGB to fractions of 1
		r, g, b = r / 255.0, g / 255.0, b / 255.0

		# Find min and max values
		cmin = min(r, g, b)
		cmax = max(r, g, b)
		delta = cmax - cmin

		# Calculate hue
		h = 0
		if delta == 0:
			h = 0
		elif cmax == r:
			h = ((g - b) / delta) % 6
		elif cmax == g:
			h = (b - r) / delta + 2
		else:
			h = (r - g) / delta + 4

		h = round(h * 60)
		if h < 0:
			h += 360

		# Calculate lightness
		l = (cmax + cmin) / 2

		# Calculate saturation
		s = 0
		if delta != 0:
			s = delta / (1 - abs(2 * l - 1))

		# Convert to percentages
		s = round(s * 100)
		l = round(l * 100)

		return (h, s, l)

	@classmethod
	def from_hsl(cls, hsl: HSLColor) -> "HexColor":
		"""
		Create a HexColor object from HSL values.

		Args:
			hsl: A tuple of three integers representing the hue (0-360),
				saturation (0-100), and lightness (0-100) components.

		Returns:
			A new HexColor object.

		Raises:
			ValueError: If any HSL component is outside the valid range.
		"""
		h, s, l = hsl

		# Validate HSL values
		if not 0 <= h <= 360:
			raise ValueError(f"Invalid hue value in {hsl}. Hue must be between 0 and 360.")

		if not 0 <= s <= 100 or not 0 <= l <= 100:
			raise ValueError(f"Invalid saturation or lightness in {hsl}. Both must be between 0 and 100.")

		# Convert to fractions
		s /= 100.0
		l /= 100.0

		# Calculate RGB
		c = (1 - abs(2 * l - 1)) * s
		x = c * (1 - abs((h / 60) % 2 - 1))
		m = l - c / 2

		r, g, b = 0, 0, 0

		if 0 <= h < 60:
			r, g, b = c, x, 0
		elif 60 <= h < 120:
			r, g, b = x, c, 0
		elif 120 <= h < 180:
			r, g, b = 0, c, x
		elif 180 <= h < 240:
			r, g, b = 0, x, c
		elif 240 <= h < 300:
			r, g, b = x, 0, c
		elif 300 <= h < 360:
			r, g, b = c, 0, x

		r = round((r + m) * 255)
		g = round((g + m) * 255)
		b = round((b + m) * 255)

		return cls.from_rgb((r, g, b))

	def to_hsla(self) -> HSLAColor:
		"""
		Convert the hex color code to HSLA format.

		Returns:
			A tuple of three integers and a float representing the hue (0-360),
			saturation (0-100), lightness (0-100), and alpha (0-1) components.
		"""
		h, s, l = self.to_hsl()
		_, _, _, a = self.to_rgba()

		return (h, s, l, a)

	@classmethod
	def from_hsla(cls, hsla: HSLAColor) -> "HexColor":
		"""
		Create a HexColor object from HSLA values.

		Args:
			hsla: A tuple of three integers and a float representing the hue (0-360),
				saturation (0-100), lightness (0-100), and alpha (0-1) components.

		Returns:
			A new HexColor object.

		Raises:
			ValueError: If any component is outside the valid range.
		"""
		h, s, l, a = hsla

		# Validate alpha
		if not 0 <= a <= 1:
			raise ValueError(f"Invalid alpha value in {hsla}. Alpha must be between 0 and 1.")

		# Create RGB hex from HSL
		rgb_hex = cls.from_hsl((h, s, l))

		# Get RGB values and add alpha
		r, g, b = rgb_hex.to_rgb()

		return cls.from_rgba((r, g, b, a))

	def to_css(self) -> "CSSNamedColor":
		"""
		Convert the hex color code to the closest CSS named color.

		Returns:
			A CSSNamedColor object representing
			the closest named color to the hex code.
		"""
		css_rgb_codes = {self.__class__(color.hex).to_rgb(): color for color in CSSNamedColor}
		return css_rgb_codes[min(css_rgb_codes, key=lambda c: euclidean(c, self.to_rgb()))]

	@classmethod
	def from_css(cls, css: "CSSNamedColor") -> "HexColor":
		"""
		Create a HexColor object from a CSS named color.

		Args:
			css: A CSSNamedColor object representing a named color.

		Returns:
			A new HexColor object.
		"""
		return cls(css.hex)
