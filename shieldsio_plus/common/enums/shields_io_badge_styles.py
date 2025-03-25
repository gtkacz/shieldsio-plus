from typing import ClassVar

from aenum import NoAlias

from shieldsio_plus.common.enums.better_enum import BetterStrEnum


class ShieldsIOBadgeStyle(BetterStrEnum):
	"""
	Enumeration of supported badge styles for Shields.io.

	This enum defines the available visual styles for Shields.io badges,
	with string values matching the API parameter values.

	Elements:
		FLAT: Standard flat style with slight gradient.
		FLAT_SQUARE: Flat style with square corners.
		PLASTIC: Style with more pronounced gradient effect.
		FOR_THE_BADGE: Larger style with uppercase text.
		SOCIAL: Style mimicking social media badges.
		TRUE_FLAT: Style that removes text shadows and color gradients from Shields.io's `flat` style
	"""

	_settings_: ClassVar = NoAlias  # Disable aliasing in the enum

	FLAT = "flat"
	FLAT_SQUARE = "flat-square"
	PLASTIC = "plastic"
	FOR_THE_BADGE = "for-the-badge"
	SOCIAL = "social"

	# Special variants that may have custom rendering in the application
	TRUE_FLAT = "flat-square"

	@property
	def styles(self) -> list[str]:
		"""Return the style names."""
		return [name.replace("_", "-").lower() for name in self.names]
