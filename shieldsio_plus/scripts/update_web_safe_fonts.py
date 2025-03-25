from argparse import ArgumentParser
from json import dump
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def script() -> None:
	"""
	Script to scrape web safe font information from CSS Font Stack.

	This script fetches web safe font information from cssfontstack.com,
	parses the data to extract font families and styles, and saves
	the processed data to a JSON file.

	Raises:
		FileExistsError: If the output file already exists and the force flag is not set.
		ValueError: If the output path format does not match the output format.
	"""
	# Set up command-line argument parser
	parser = ArgumentParser(description="Scrape web safe fonts from CSS Font Stack.")

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

	# Parse arguments
	args = parser.parse_args()

	# Print help if no arguments provided
	if not args:
		parser.print_help()

	# Create output directory if it doesn't exist
	output_dir = Path("/".join(args.output_path.split("/")[:-1]))
	if not output_dir.exists():
		output_dir.mkdir(parents=True, exist_ok=True)

	# Check if output file exists and force flag is not set
	if Path(args.output_path).exists() and not args.force:
		raise FileExistsError(f"Output path already exists: {args}.")

	# Validate output format is JSON
	if args.output_path.split(".")[-1] != "json":
		raise ValueError(f"Output path format does not match the output format: {args}.")

	# Target URL for scraping
	target_url = "https://www.cssfontstack.com/"

	# Map of font family types to their corresponding div IDs on the page
	div_map: dict[str, str] = {
		"sans-serif": "dashboard-sans-serif",
		"serif": "dashboard-serif",
		"monospaced": "dashboard-monospaced",
		"fantasy": "dashboard-fantasy",
		"script": "dashboard-script",
	}

	# Map of family name aliases to standardize terminology
	aliases: dict[str, str] = {"monospaced": "monospace", "script": "cursive"}

	# Fetch and parse HTML
	html = requests.get(target_url, timeout=60).text
	soup = BeautifulSoup(html, "html.parser")

	# Initialize dictionary to store font data by family
	parsed_fonts: dict[str, list[dict[str, str]]] = {aliases.get(family, family): [] for family in div_map}

	# Extract font information for each family type
	for key, value in div_map.items():
		# Find the div container for this font family
		div = soup.find("div", {"id": value})

		# Find all font entries
		fonts = div.find_all("div", {"class": "ow-server"})

		# Extract style attribute containing font-family definitions
		fonts = [font.find("h4")["style"] for font in fonts]

		# Parse font information into a structured format
		fonts_map = [
			{
				"family-name": font.split(",")[0].replace("font-family: ", "").replace('"', ""),
				"style": font,
			}
			for font in fonts
		]

		# Add fonts to the appropriate family category, using aliases if needed
		parsed_fonts[aliases.get(key, key)] += fonts_map

	# Write parsed font data to JSON file
	with Path(args.output_path).open("w", encoding="utf-8") as file:
		dump(parsed_fonts, file, indent=4)


if __name__ == "__main__":
	script()
