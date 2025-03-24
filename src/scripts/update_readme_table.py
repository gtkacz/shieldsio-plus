import json
from argparse import ArgumentParser
from pathlib import Path

from loguru import logger


def script() -> None:
	"""
	Script to update a markdown file with a table of badge slugs.

	This script reads badge data from a JSON file, extracts unique slugs,
	and updates a README.md file with a formatted table showing each slug
	and its corresponding SVG badge image.
	"""
	# Set up command-line argument parser
	parser = ArgumentParser(description="Update README.md with badge slugs from JSON data.")

	parser.add_argument(
		"--markdown_filename",
		type=str,
		default="README.md",
		help="Path to the markdown filename to be updated.",
		required=False,
	)

	parser.add_argument(
		"--json_filename",
		type=str,
		default="assets/data/badges.json",
		help="Path to the JSON filename to be read.",
		required=False,
	)

	# Parse arguments
	args = parser.parse_args()

	# Print help if no arguments provided
	if not args:
		parser.print_help()

	# Read badge data from JSON file
	with Path(args.json_filename).resolve().open(encoding="utf-8") as f:
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
	with Path(args.markdown_filename).resolve().open(encoding="utf-8") as f:
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
	with Path(args.markdown_filename).resolve().open("w", encoding="utf-8") as f:
		f.write(new_content)

	# Print status message
	logger.info(f"Updated {args.markdown_filename} with {len(unique_slugs)} unique slugs.")


if __name__ == "__main__":
	script()
