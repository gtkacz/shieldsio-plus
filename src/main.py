import pathlib

from src.common.types.esio_file import ESIOFile
from src.common.types.hex_code import HexCode
from src.util import svg_to_base64, download_shields_io_badges

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


def main():
	parsed_data = []
	all_svgs = list(pathlib.Path(f"{BASE_DIR}/assets/icons").glob("*.svg"))

	for svg in all_svgs:
		slug, display_text, bg_color = svg.stem.split("_")

		parsed_data.append(
			ESIOFile(
				slug,
				display_text,
				HexCode(bg_color),
				svg_to_base64(svg),
			)
		)

	download_shields_io_badges(parsed_data, f"{BASE_DIR}/assets/shields")


if __name__ == "__main__":
	main()
