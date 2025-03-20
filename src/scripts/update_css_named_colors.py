from argparse import ArgumentParser
from functools import partial
from pathlib import Path

import pandas as pd

from src.common.types.hex_code import HexColor


def script() -> None:
	parser = ArgumentParser()

	parser.add_argument(
		"--output-path",
		type=str,
		default="data/css_named_colors.json",
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

	args = parser.parse_args()

	if not args:
		parser.print_help()

	if not Path("/".join(args.output_path.split("/")[:-1])).exists():
		Path("/".join(args.output_path.split("/")[:-1])).mkdir(parents=True, exist_ok=True)

	if Path(args.output_path).exists() and not args.force:
		raise FileExistsError(f"Output path already exists: {args}.")

	if args.output_format != args.output_path.split(".")[-1]:
		raise ValueError(f"Output path format does not match the output format: {args}.")

	if args.output_format == "json":
		output_method = partial(pd.DataFrame.to_json, orient="records")
	elif args.output_format == "csv":
		output_method = partial(pd.DataFrame.to_csv, index=False)
	else:
		raise ValueError(f"Invalid output format: {args.output_format}")

	dfs = pd.read_html(args.url)
	basic_colors, extended_colors = dfs[0], dfs[1]
	all_colors = pd.concat([basic_colors, extended_colors])[[args.slug_column_name, args.hex_column_name]].dropna()
	all_colors.columns = ["slug", "hex"]

	all_colors = all_colors[all_colors["slug"] != "transparent"]

	all_colors["slug"] = all_colors["slug"].str.replace(" ", "-").str.lower()
	all_colors["hex"] = all_colors["hex"].str.split(" ").str[0].apply(HexColor)
	all_colors["rgb"] = all_colors["hex"].apply(HexColor.to_rgb)
	all_colors["rgba"] = all_colors["hex"].apply(HexColor.to_rgba)
	all_colors["hsl"] = all_colors["hex"].apply(HexColor.to_hsl)
	all_colors["hsla"] = all_colors["hex"].apply(HexColor.to_hsla)
	all_colors["hex"] = all_colors["hex"].apply(str)

	output_method(all_colors, args.output_path)


if __name__ == "__main__":
	script()
