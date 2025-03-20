import pathlib

from src.common.enums.shields_io_badge_types import ShieldsIOBadgeStyles
from src.common.types.hex_code import HexColor
from src.common.types.shields_io_badge import ShieldsIOBadge
from src.util import read_svg
from src.util.download_shieldsio_badges import download_shields_io_badges

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


def main():
	parsed_data = []
	all_svgs = list(pathlib.Path(f"{BASE_DIR}/assets/icons").glob("*.svg"))

	for svg in all_svgs:
		slug, display_text, bg_color = svg.stem.split("_")

		for style in ShieldsIOBadgeStyles:
			parsed_data.append(
				ShieldsIOBadge(
					slug=slug,
					label=display_text,
					color=HexColor(bg_color),
					logo=read_svg(svg),
					style=style
				),
			)

	download_shields_io_badges(parsed_data, f"{BASE_DIR}/assets/", f"{BASE_DIR}/data/badges.json")


if __name__ == "__main__":
	main()
