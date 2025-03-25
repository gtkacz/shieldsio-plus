import json
from argparse import ArgumentParser
from collections.abc import Sequence
from pathlib import Path
from typing import Optional

from loguru import logger

from shieldsio_plus.common.enums.web_safe_fonts import WebSafeFont


def update_available_logos(markdown_filename: str, badges_json_filename: str) -> None:
	# Read badge data from JSON file
	with Path(badges_json_filename).open(encoding="utf-8") as f:
		data = json.load(f)

	# Extract unique slugs
	seen: set[str] = set()
	unique_slugs: list[str] = []

	for item in data:
		slug = item.get("slug")

		if slug and slug not in seen:
			seen.add(slug)
			unique_slugs.append(slug)

	# Sort slugs alphabetically
	unique_slugs.sort()

	# Generate new table content
	new_table_lines: list[str] = []
	new_table_lines.append("| Slug | Sample |")
	new_table_lines.append("| --- | --- |")

	new_table_lines.extend([f"| {slug} | ![{slug}](./assets/shields/flat/{slug}.svg) |" for slug in unique_slugs])

	new_table = "\n".join(new_table_lines)

	# Read current README.md content
	with Path(markdown_filename).open(encoding="utf-8") as f:
		lines = f.readlines()

	# Process file and replace table
	new_lines: list[str] = []
	i = 0

	while i < len(lines):
		line = lines[i]
		new_lines.append(line.rstrip("\n"))

		# Found the section header for available slugs
		if line.strip() == "#### Available Slugs":
			i += 1

			# Skip any blank line after the header
			if i < len(lines) and not lines[i].strip():
				new_lines.append(lines[i].rstrip("\n"))
				i += 1

			# Skip existing table rows
			while i < len(lines) and lines[i].lstrip().startswith("|"):
				i += 1

			# Insert new table
			new_lines.append(new_table)
			continue

		i += 1

	# Join content and ensure there's a trailing newline
	new_content = "\n".join(new_lines) + "\n"

	# Write updated content back to the file
	with Path(markdown_filename).open("w", encoding="utf-8") as f:
		f.write(new_content)

	# Print status message
	logger.info(f"Updated {markdown_filename} with {len(unique_slugs)} unique slugs.")


def update_available_fonts(markdown_filename: str) -> None:
	# Read badge data from JSON file
	all_fonts = sorted(WebSafeFont.members, key=lambda x: x.family_name)

	# Generate new table content
	new_table_lines: list[str] = []
	new_table_lines.append("| Family Name | Type | Sample |")
	new_table_lines.append("| --- | --- | --- |")

	for font in all_fonts:
		if font != WebSafeFont.DEFAULT:
			line = f"| {font.family_name.title()} | {font.family.value.title()} | ![twitter](./assets/shields/flat/{font.name.lower()}/twitter.svg) |"  # noqa: E501
			new_table_lines.append(line)

	new_table = "\n".join(new_table_lines)

	# Read current README.md content
	with Path(markdown_filename).open(encoding="utf-8") as f:
		lines = f.readlines()

	# Process file and replace table
	new_lines: list[str] = []
	i = 0

	while i < len(lines):
		line = lines[i]
		new_lines.append(line.rstrip("\n"))

		# Found the section header for available slugs
		if line.strip() == "#### Available Fonts":
			i += 1

			# Skip any blank line after the header
			if i < len(lines) and not lines[i].strip():
				new_lines.append(lines[i].rstrip("\n"))
				i += 1

			# Skip existing table rows
			while i < len(lines) and lines[i].lstrip().startswith("|"):
				i += 1

			# Insert new table
			new_lines.append(new_table)
			continue

		i += 1

	# Join content and ensure there's a trailing newline
	new_content = "\n".join(new_lines) + "\n"

	# Write updated content back to the file
	with Path(markdown_filename).open("w", encoding="utf-8") as f:
		f.write(new_content)

	# Print status message
	logger.info(f"Updated {markdown_filename} with {len(all_fonts)} unique fonts.")


def script(args: Optional[Sequence[str]] = None) -> None:
	"""
	Script to update a markdown file with a table of badge slugs.

	This script reads badge data from a JSON file, extracts unique slugs,
	and updates a README.md file with a formatted table showing each slug
	and its corresponding SVG badge image.
	"""
	# Set up command-line argument parser
	parser = ArgumentParser(description="Update README.md with badge slugs from JSON data.")

	parser.add_argument(
		"--markdown-filename",
		type=str,
		default="README.md",
		help="Path to the markdown filename to be updated.",
		required=False,
	)

	parser.add_argument(
		"--badges-json-filename",
		type=str,
		default="assets/data/badges.json",
		help="Path to the JSON filename to be read.",
		required=False,
	)

	# Parse arguments
	args = parser.parse_args(args)

	# Print help if no arguments provided
	if not args:
		parser.print_help()

	# Run the scripts
	update_available_logos(args.markdown_filename, args.badges_json_filename)
	update_available_fonts(args.markdown_filename)


if __name__ == "__main__":
	script()
