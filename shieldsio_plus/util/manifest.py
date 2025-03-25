import json
from pathlib import Path
from typing import Optional, TypedDict

from loguru import logger

from shieldsio_plus.common.enums.css_named_colors import CSSNamedColor
from shieldsio_plus.common.enums.shields_io_badge_styles import ShieldsIOBadgeStyle
from shieldsio_plus.common.enums.shields_io_named_colors import ShieldsIONamedColor
from shieldsio_plus.common.enums.web_safe_fonts import WebSafeFont
from shieldsio_plus.common.types.hex_code import HexColor
from shieldsio_plus.common.types.svg import SVG


class ManifestColor(TypedDict):
	"""Definition of a color dictionary in the manifest."""

	class_: str
	value: str


def validate_manifest(path: str = "assets/data/manifest.json") -> None:  # noqa: C901
	"""
	Validate the manifest file.

	Args:
		path (optional): Path to the manifest file. Defaults to "assets/data/manifest.json".

	Raises:
		ValueError: The manifest file failed to validate.
	"""  # noqa: DOC501, DOC502

	def _validate_color(color: Optional[ManifestColor], *, check_for_none: bool = True) -> Optional[ValueError]:
		if not color:
			if check_for_none:
				return ValueError("Color is `null`")

			return None

		if "class" not in color or "value" not in color:
			return ValueError(f"Missing `class` or `value` keys in {color}")

		if color["class"] not in HexColor.supported_classes:
			return ValueError(f"Invalid color class: {color['class']}, should be one of {HexColor.supported_classes}")

		try:
			load_manifest_color(color)

		except ValueError as e:
			return e

	with Path(path).open(encoding="utf-8") as f:
		manifest = json.load(f)

	found_errors = []

	slugs = [dic["slug"] for dic in manifest["data"]]

	if not Path(manifest["root"]).exists() or not Path(manifest["root"]).is_dir():
		found_errors.append(ValueError(f"Root directory {manifest['root']} does not exist or is not a directory"))

	if len(set(slugs)) != len(slugs):
		found_errors.append(ValueError(f"Duplicate slugs found: { {item for item in slugs if slugs.count(item) > 1} }"))

	root_dir = manifest["root"]

	for dic in manifest["data"]:
		if "slug" not in dic:
			found_errors.append(ValueError(f"Missing slug in {dic}"))

		try:
			SVG.from_file(root_dir + dic["logo"])
		except ValueError as e:
			found_errors.append(e)

		if dic.get("style", None) and dic["style"] not in ShieldsIOBadgeStyle.styles:
			found_errors.append(ValueError(f"Invalid style: {dic['style']}"))

		if dic.get("font", None) and dic["font"] not in WebSafeFont.family_names:
			found_errors.append(ValueError(f"Invalid font: {dic['font']}"))

		if error := _validate_color(dic.get("color", None)):
			found_errors.append(error)

		if error := _validate_color(dic.get("label_color", None), check_for_none=False):
			found_errors.append(error)

		if error := _validate_color(dic.get("logo_color", None), check_for_none=False):
			found_errors.append(error)

	if found_errors:
		raise ExceptionGroup("Failed to validate", found_errors)

	logger.debug(f"Manifest validated successfully from {path}")


def load_manifest_color(color: ManifestColor) -> HexColor:  # noqa: PLR0911, RET503
	"""
	Load a color from the manifest.

	Args:
		color: The color to load.

	Raises:
		ValueError: The named color is invalid.

	Returns:
		The loaded color.
	"""
	if color["class"] == "hex":
		return HexColor(color["value"])

	if color["class"] == "rgb":
		return HexColor.from_rgb(color["value"])

	if color["class"] == "rgba":
		return HexColor.from_rgba(color["value"])

	if color["class"] == "hsl":
		return HexColor.from_hsl(color["value"])

	if color["class"] == "hsla":
		return HexColor.from_hsla(color["value"])

	if color["class"] == "named_color":
		if color["value"] in ShieldsIONamedColor.slugs():
			return HexColor.from_css(ShieldsIONamedColor(color["value"].replace("-", "_").upper()))

		if color["value"] in CSSNamedColor.names:
			return HexColor.from_css(CSSNamedColor(color["value"].replace("-", "_").upper()))

		raise ValueError(f"Invalid named color: {color['value']}")
