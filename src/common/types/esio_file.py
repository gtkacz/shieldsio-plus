from dataclasses import dataclass

from src.util import is_valid_base_64, is_valid_hex_code


@dataclass(frozen=True)
class ESIOFile:
	slug: str
	display_text: str
	bg_color: str
	base64: bytes

	def __post_init__(self):
		if not is_valid_hex_code(self.bg_color):
			raise ValueError(f"Invalid hex code: {self.bg_color}")

		if not is_valid_base_64(self.base64):
			raise ValueError(f"Invalid base64 data: {self.base64}")
