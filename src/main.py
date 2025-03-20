import pathlib

from src.util import svg_to_base64

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

from pprint import pprint

print = pprint


def main():
	parsed_data = []
	all_svgs = list(pathlib.Path(f"{BASE_DIR}/assets/icons").glob("*.svg"))

	for svg in all_svgs:
		slug, display_text, bg_color = svg.stem.split("_")

		parsed_data.append({
			"slug": slug,
			"display_text": display_text,
			"bg_color": bg_color,
			"base64": svg_to_base64(svg),
		})

	print(parsed_data)

	shields_io_base_url = "https://img.shields.io/badge/{}-{}.svg?style={}&logo=data:image/svg%2bxml;base64,{}"


if __name__ == "__main__":
	main()
