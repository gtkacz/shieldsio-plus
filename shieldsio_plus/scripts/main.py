import pathlib

from shieldsio_plus.common.enums.shields_io_badge_styles import ShieldsIOBadgeStyle
from shieldsio_plus.common.enums.web_safe_fonts import WebSafeFont
from shieldsio_plus.common.types.hex_code import HexColor
from shieldsio_plus.common.types.shields_io_badge import ShieldsIOBadge
from shieldsio_plus.common.types.svg import SVG
from shieldsio_plus.util.download_shieldsio_badges import download_shields_io_badges

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


def main() -> None:
	parsed_data = []
	all_svgs = list(pathlib.Path(f"{BASE_DIR}/assets/icons").glob("*.svg"))

	for svg in all_svgs:
		slug, display_text, bg_color = svg.stem.split("_")

		parsed_data.extend([
			ShieldsIOBadge(
				slug=slug,
				label=display_text,
				color=HexColor(bg_color),
				logo=SVG.from_file(svg),
				style=ShieldsIOBadgeStyle[style.name],
			)
			for style in ShieldsIOBadgeStyle.members
		])

	for font in WebSafeFont:
		svg = next(svg for svg in all_svgs if "windows-10-blue" in svg.stem)
		slug, display_text, bg_color = svg.stem.split("_")

		parsed_data.extend([
			ShieldsIOBadge(
				slug=slug,
				label=display_text,
				color=HexColor(bg_color),
				logo=SVG.from_file(svg),
				font=font,
			),
		])

	download_shields_io_badges(parsed_data, f"{BASE_DIR}/assets/shields/", f"{BASE_DIR}/assets/data/badges.json")


if __name__ == "__main__":
	main()
