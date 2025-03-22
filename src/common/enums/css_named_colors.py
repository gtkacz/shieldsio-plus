import json

from src.common.enums.better_enum import BetterEnum
from src.common.types.hex_code import HexColor

with open("assets/data/css_named_colors.json") as f:
	data = json.load(f)

data = list({item["slug"].upper(): HexColor(item["hex"]) for item in data}.items())

CSSNamedColor = BetterEnum("CSSNamedColor", data)
