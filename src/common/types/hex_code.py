from dataclasses import dataclass
from src.util import is_valid_hex_code


@dataclass(frozen=True)
class HexCode:
	value: str

	def __init__(self, value: str):
		processed_value = value if not value.startswith("#") else value[1:]
		object.__setattr__(self, "value", processed_value)

		if not is_valid_hex_code(self.value):
			raise ValueError(f"Invalid hex code: {self.value}")

	@property
	def hex(self) -> str:
		return "#" + self.value
