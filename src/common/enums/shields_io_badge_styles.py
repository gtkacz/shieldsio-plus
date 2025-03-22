from aenum import NoAlias

from src.common.enums.better_enum import BetterStrEnum


class ShieldsIOBadgeStyle(BetterStrEnum):
	_settings_ = NoAlias

	FLAT = "flat"
	FLAT_SQUARE = "flat-square"
	PLASTIC = "plastic"
	FOR_THE_BADGE = "for-the-badge"
	SOCIAL = "social"

	TRUE_FLAT = "flat"
	TRUE_FLAT_SQUARE = "flat-square"
