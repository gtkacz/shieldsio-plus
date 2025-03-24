import pathlib
from json import dumps

from pyperclip import copy

parsed_data = []
all_svgs = list(pathlib.Path("./assets/icons").glob("*.svg"))

for svg in all_svgs:
	slug, display_text, bg_color = svg.stem.split("_")
	parsed_data.append(
		{
			"logo": str(svg),
			"slug": slug,
			"label": display_text,
			"message": None,
			"style": None,
			"color": bg_color,
			"label_color": None,
			"logo_color": None,
			"font": None,
		},
	)

copy(dumps(parsed_data))
