import json
from pathlib import Path

from shieldsio_plus.common.enums.better_enum import BetterEnum


class _UnicodeRange(BetterEnum):
	"""Enumeration of Unicode ranges for use in web applications."""

	@property
	def slug(self) -> str:
		"""The Unicode block slug."""
		return self.name.replace("_", "-").lower()

	@property
	def block(self) -> str:
		"""The Unicode block name."""
		return self.name

	@property
	def range(self) -> str:
		"""The Unicode block range."""
		return self.value


# Load unicode ranges definitions from JSON file
with Path("assets/data/unicode_ranges.json").open(encoding="utf-8") as f:
	data = json.load(f)

data = list({item["block"].replace("-", "_").upper(): item["range"] for item in data}.items())

if len({key for key, _ in data}) != len(data):
	raise ValueError("Duplicate Unicode block names found")

# Dynamically create the UnicodeRange enum with the processed data
UnicodeRange = _UnicodeRange("UnicodeRange", data)
