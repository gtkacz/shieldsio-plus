from base64 import b64decode, b64encode
from dataclasses import dataclass
from warnings import warn
from xml.etree import ElementTree as ET


@dataclass
class SVG:
	svg_str: str
	b64: str = ""

	def __post_init__(self):
		if not self.svg_str:
			raise ValueError("SVG content cannot be empty")

		if self.b64:
			warn("Base64 data is provided, but it will be ignored", UserWarning)

		self.svg_to_base64()

		if not self.is_valid_base_64(self.b64):
			raise ValueError(f"Invalid base64 data: {self.b64}")

	@classmethod
	def from_file(cls, path: str):
		with open(path) as handler:
			return cls(handler.read())

	def svg_to_base64(self) -> str:
		self.b64 = b64encode(self.svg_str.encode()).decode()

	@property
	def svg(self) -> str:
		return self.svg_str

	@property
	def base64(self) -> str:
		return self.b64

	@staticmethod
	def is_valid_base_64(data: str) -> bool:
		if not isinstance(data, str):
			return False

		try:
			b64decode(data.encode(), validate=True)
			return True
		except Exception:
			return False

	@staticmethod
	def local_name(tag):
		return tag.split("}")[-1] if "}" in tag else tag

	@staticmethod
	def remove_linear_gradients(parent):
		for child in list(parent):
			if SVG.local_name(child.tag) == "linearGradient":
				parent.remove(child)
			else:
				SVG.remove_linear_gradients(child)

	@staticmethod
	def remove_shadow_texts(parent):
		"""
		Recursively remove text elements that seem to be used as shadows.
		Here we assume any <text> with aria-hidden="true" or a fill-opacity attribute not equal to "1"
		is a shadow.
		"""
		for child in list(parent):
			if SVG.local_name(child.tag) == "text":
				if child.attrib.get("aria-hidden") == "true" or (
					child.attrib.get("fill-opacity") and child.attrib.get("fill-opacity") != "1"
				):
					parent.remove(child)
				else:
					SVG.remove_shadow_texts(child)
			else:
				SVG.remove_shadow_texts(child)

	def parse_real_flat(self) -> None:
		root = ET.fromstring(self.svg_str)

		self.remove_linear_gradients(root)
		self.remove_shadow_texts(root)

		self.svg_str = ET.tostring(root, encoding="unicode")

	def change_svg_color(self, color: str) -> None:
		"""
		Change the color of the SVG to the provided color.
		"""
		root = ET.fromstring(self.svg_str)

		for child in root.iter():
			if SVG.local_name(child.tag) == "path":
				if "fill" in child.attrib:
					child.attrib["fill"] = color

		self.svg_str = ET.tostring(root, encoding="unicode")
