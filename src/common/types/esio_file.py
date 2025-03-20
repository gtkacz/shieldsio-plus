from dataclasses import dataclass

from src.common.types.hex_code import HexColor
from src.common.types.shields_io_badge import ShieldsIOBadge
from src.util import is_valid_base_64


@dataclass(frozen=True)
class ESIOFile:
	slug: str
	display_text: str
	bg_color: HexColor
	base64: bytes

	def __post_init__(self):
		if not is_valid_base_64(self.base64):
			raise ValueError(f"Invalid base64 data: {self.base64}")

	def to_shields_io_badge(self) -> ShieldsIOBadge:
		return ShieldsIOBadge(
			slug=self.slug,
			label=self.display_text,
			logo=self.base64,
			color=self.bg_color,
		)
