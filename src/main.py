import pathlib

from src.common.enums.shields_io_badge_styles import ShieldsIOBadgeStyle
from src.common.types.hex_code import HexColor
from src.common.types.shields_io_badge import ShieldsIOBadge
from src.common.types.svg import SVG
from src.util.download_shieldsio_badges import download_shields_io_badges

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


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

	download_shields_io_badges(parsed_data, f"{BASE_DIR}/assets/shields/", f"{BASE_DIR}/assets/data/badges.json")


if __name__ == "__main__":
	main()
