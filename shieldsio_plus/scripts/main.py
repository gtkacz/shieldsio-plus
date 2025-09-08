from json import load as json_load
from operator import itemgetter
from pathlib import Path

from shieldsio_plus.common.enums.shields_io_badge_styles import ShieldsIOBadgeStyle
from shieldsio_plus.common.enums.web_safe_fonts import WebSafeFont
from shieldsio_plus.common.types.shields_io_badge import ShieldsIOBadge
from shieldsio_plus.common.types.svg import SVG
from shieldsio_plus.scripts.update_readme import script as update_readme
from shieldsio_plus.util.download_shieldsio_badges import download_shields_io_badges
from shieldsio_plus.util.manifest import load_manifest_color, validate_manifest
from shieldsio_plus.util.metadata import should_run, write_metadata

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def script() -> None:
	manifest_path = f"{BASE_DIR}/assets/data/manifest.json"
	metadata_path = f"{BASE_DIR}/assets/data/metadata"

	validate_manifest(manifest_path)

	if not should_run(manifest_path, metadata_path):
		return

	with Path(manifest_path).open("r", encoding="utf-8") as f:
		manifest = json_load(f)

	parsed_data = []

	for logo in manifest["data"]:
		path = str(BASE_DIR) + "/" + manifest["root"] + logo["logo"]

		params = {
			"slug": logo["slug"],
			"label": logo["label"],
			"logo": SVG.from_file(path),
			"message": logo["message"],
			"color": load_manifest_color(logo["color"]),
			"label_color": load_manifest_color(logo["label_color"]) if logo.get("label_color", None) else None,
			"logo_color": load_manifest_color(logo["logo_color"]) if logo.get("logo_color", None) else None,
			"font": WebSafeFont.from_family_name(logo["logo_font"])
			if logo.get("logo_font", None)
			else WebSafeFont.DEFAULT,
		}

		parsed_data.extend([
			ShieldsIOBadge(
				**dict(filter(itemgetter(1), params.items())),
				style=ShieldsIOBadgeStyle[style.name],
			)
			for style in ShieldsIOBadgeStyle.members
		])

	font_logo = next(dic for dic in manifest["data"] if dic["slug"] == "twitter")

	for font in WebSafeFont:
		path = str(BASE_DIR) + "/" + manifest["root"] + font_logo["logo"]

		params = {
			"slug": font_logo["slug"],
			"label": font_logo["label"],
			"logo": SVG.from_file(path),
			"message": font_logo["message"],
			"style": ShieldsIOBadgeStyle.FLAT,
			"color": load_manifest_color(font_logo["color"]),
			"label_color": load_manifest_color(font_logo["label_color"])
			if font_logo.get("label_color", None)
			else None,
			"logo_color": load_manifest_color(font_logo["logo_color"]) if font_logo.get("logo_color", None) else None,
			"font": font,
		}

		parsed_data.append(ShieldsIOBadge(**dict(filter(itemgetter(1), params.items()))))

	download_shields_io_badges(parsed_data, f"{BASE_DIR}/assets/shields/", f"{BASE_DIR}/assets/data/badges.json")
	write_metadata(metadata_path)
	update_readme()


if __name__ == "__main__":
	script()
