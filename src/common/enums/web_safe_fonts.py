import json

from src.common.enums.better_enum import BetterEnum


class WebSafeFont(BetterEnum):
	@classmethod
	def get_values_by_key(cls, key):
		return [d for d in cls.values if d["family"] == key]

	@property
	def family_name(self):
		return self.value["family-name"]

	@property
	def style(self):
		return self.value["style"]

	@property
	def family(self):
		return self.value["family"]


class FontFamily(BetterEnum):
	@property
	def fonts(self):
		return WebSafeFont.get_values_by_key(self)


with open("assets/data/web_safe_fonts.json") as f:
	raw_data = json.load(f)

families_data = list({value.replace("-", "_").upper(): value for value in raw_data.keys()}.items())
FontFamily = FontFamily("FontFamily", families_data)

fonts_data = list(
	{
		d["family-name"].replace(" ", "_").upper(): d | {"family": FontFamily(d["style"].split(",")[-1].split(";")[0])}
		for d in [item for sublist in raw_data.values() for item in sublist]
	}.items(),
)

fonts_data.append((
	"DEFAULT",
	{
		"family-name": "Default",
		"style": "Verdana,Geneva,DejaVu Sans,sans-serif !important",
		"family": FontFamily.SANS_SERIF,
	},
))

WebSafeFont = WebSafeFont("WebSafeFont", fonts_data)
