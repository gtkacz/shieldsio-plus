from typing import ClassVar

from aenum import NoAlias

from src.common.enums.better_enum import BetterStrEnum


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
		TRUE_FLAT_SQUARE: Style that removes text shadows and color gradients from Shields.io's `flat-square` style
	"""

	_settings_: ClassVar = NoAlias  # Disable aliasing in the enum

	FLAT = "flat"
	FLAT_SQUARE = "flat-square"
	PLASTIC = "plastic"
	FOR_THE_BADGE = "for-the-badge"
	SOCIAL = "social"

	# Special variants that may have custom rendering in the application
	TRUE_FLAT = "flat"
	TRUE_FLAT_SQUARE = "flat-square"
