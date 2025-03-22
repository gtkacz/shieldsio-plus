from argparse import ArgumentParser
from json import dump
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def script() -> None:
	parser = ArgumentParser()

	parser.add_argument(
		"--output-path",
		type=str,
		default="assets/data/web_safe_fonts.json",
		help="Output path for the web safe fonts data.",
		required=False,
	)

	parser.add_argument(
		"--force",
		action="store_true",
		default=False,
		help="Force overwrite the existing web safe fonts data.",
		required=False,
	)

	args = parser.parse_args()

	if not args:
		parser.print_help()

	if not Path("/".join(args.output_path.split("/")[:-1])).exists():
		Path("/".join(args.output_path.split("/")[:-1])).mkdir(parents=True, exist_ok=True)

	if Path(args.output_path).exists() and not args.force:
		raise FileExistsError(f"Output path already exists: {args}.")

	if args.output_path.split(".")[-1] != "json":
		raise ValueError(f"Output path format does not match the output format: {args}.")

	target_url = "https://www.cssfontstack.com/"

	div_map = {
		"sans-serif": "dashboard-sans-serif",
		"serif": "dashboard-serif",
		"monospaced": "dashboard-monospaced",
		"fantasy": "dashboard-fantasy",
		"script": "dashboard-script",
	}

	aliases = {"monospaced": "monospace", "script": "cursive"}

	html = requests.get(target_url).text
	soup = BeautifulSoup(html, "html.parser")

	parsed_fonts = {aliases.get(family, family): [] for family in div_map}

	for key, value in div_map.items():
		div = soup.find("div", {"id": value})
		fonts = div.find_all("div", {"class": "ow-server"})
		fonts = [font.find("h4")["style"] for font in fonts]

		fonts_map = [
			{
				"family-name": font.split(",")[0].replace("font-family: ", "").replace('"', ""),
				"style": font,
			}
			for font in fonts
		]

		parsed_fonts[aliases.get(key, key)] += fonts_map

	with open(args.output_path, "w") as file:
		dump(parsed_fonts, file, indent=4)


if __name__ == "__main__":
	script()
