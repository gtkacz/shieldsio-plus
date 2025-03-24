from argparse import ArgumentParser
from functools import partial
from pathlib import Path

import pandas as pd

from shieldsio_plus.common.types.hex_code import HexColor


def script() -> None:
	"""
	Script to scrape and process CSS named colors.

	This script fetches color definitions, processes them to extract
	slug and hex values, and converts them to various color formats (RGB, RGBA, HSL, HSLA).
	The processed data is then saved to a file in the specified format.

	Raises:
		FileExistsError: If the output file already exists and the force flag is not set.
		ValueError: If the output format does not match the file extension or an invalid output format is provided.
	"""
	# Set up command-line argument parser
	parser = ArgumentParser(description="Scrape and process CSS named colors from MDN.")

	parser.add_argument(
		"--output-path",
		type=str,
		default="assets/data/css_named_colors.json",
		help="Output path for the CSS named colors data.",
		required=False,
	)

	parser.add_argument(
		"--output-format",
		type=str,
		default="json",
		choices=["json", "csv"],
		help="Output format for the CSS named colors data.",
		required=False,
	)

	parser.add_argument(
		"--url",
		type=str,
		default="https://developer.mozilla.org/en-US/docs/Web/CSS/named-color",
		help="URL to scrape the CSS named colors data.",
		required=False,
	)

	parser.add_argument(
		"--slug-column-name",
		type=str,
		default="Keyword",
		help="Column name for the CSS named colors slug.",
		required=False,
	)

	parser.add_argument(
		"--hex-column-name",
		type=str,
		default="RGB hex value",
		help="Column name for the CSS named colors hex code.",
		required=False,
	)

	parser.add_argument(
		"--force",
		action="store_true",
		default=False,
		help="Force overwrite the existing CSS named colors data.",
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

	# Validate output format matches file extension
	if args.output_format != args.output_path.split(".")[-1]:
		raise ValueError(f"Output path format does not match the output format: {args}.")

	# Set up output method based on format
	if args.output_format == "json":
		output_method = partial(pd.DataFrame.to_json, orient="records")
	elif args.output_format == "csv":
		output_method = partial(pd.DataFrame.to_csv, index=False)
	else:
		raise ValueError(f"Invalid output format: {args.output_format}")

	# Scrape tables from MDN
	dfs = pd.read_html(args.url)

	# Extract basic and extended color tables
	basic_colors, extended_colors = dfs[0], dfs[1]

	# Combine tables and select relevant columns
	all_colors = pd.concat([basic_colors, extended_colors])[[args.slug_column_name, args.hex_column_name]].dropna()
	all_colors.columns = ["slug", "hex"]

	# Remove 'transparent' as it's not a color with a hex value
	all_colors = all_colors[all_colors["slug"] != "transparent"]

	# Process color data
	# Convert spaces in slug to hyphens and make lowercase
	all_colors["slug"] = all_colors["slug"].str.replace(" ", "-").str.lower()

	# Convert hex strings to HexColor objects and extract first hex code if multiple are present
	all_colors["hex"] = all_colors["hex"].str.split(" ").str[0].apply(HexColor)

	# Generate different color format representations
	all_colors["rgb"] = all_colors["hex"].apply(HexColor.to_rgb)
	all_colors["rgba"] = all_colors["hex"].apply(HexColor.to_rgba)
	all_colors["hsl"] = all_colors["hex"].apply(HexColor.to_hsl)
	all_colors["hsla"] = all_colors["hex"].apply(HexColor.to_hsla)

	# Convert HexColor objects back to strings for serialization
	all_colors["hex"] = all_colors["hex"].apply(str)

	# Write to output file
	output_method(all_colors, args.output_path)


if __name__ == "__main__":
	script()
