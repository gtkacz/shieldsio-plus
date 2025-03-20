import json
from argparse import ArgumentParser


def script() -> None:
	parser = ArgumentParser()

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

	args = parser.parse_args()

	if not args:
		parser.print_help()

	with open(args.json_filename, encoding="utf-8") as f:
		data = json.load(f)

	seen = set()
	unique_slugs = []

	for item in data:
		slug = item.get("slug")

		if slug and slug not in seen:
			seen.add(slug)
			unique_slugs.append(slug)

	unique_slugs.sort()
	new_table_lines = []
	new_table_lines.append("| Slug | Sample |")
	new_table_lines.append("| --- | --- |")

	for slug in unique_slugs:
		new_table_lines.append(f"| {slug} | ![{slug}](./assets/shields/true_flat/{slug}.svg) |")

	new_table = "\n".join(new_table_lines)

	with open(args.markdown_filename, encoding="utf-8") as f:
		lines = f.readlines()

	new_lines = []

	i = 0

	while i < len(lines):
		line = lines[i]
		new_lines.append(line.rstrip("\n"))

		if line.strip() == "#### Available Slugs":
			i += 1

			if i < len(lines) and lines[i].strip() == "":
				new_lines.append(lines[i].rstrip("\n"))
				i += 1

			while i < len(lines) and lines[i].lstrip().startswith("|"):
				i += 1

			new_lines.append(new_table)
			continue

		i += 1

	new_content = "\n".join(new_lines) + "\n"

	with open(args.markdown_filename, "w", encoding="utf-8") as f:
		f.write(new_content)

	print(f"Updated {args.markdown_filename} with {len(unique_slugs)} unique slugs.")


if __name__ == "__main__":
	script()
