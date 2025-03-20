from typing import TypedDict, Union


class _RGBColor(TypedDict):
	r: int
	g: int
	b: int


class _RGBAColor(TypedDict):
	r: int
	g: int
	b: int
	a: float


class _HSLColor(TypedDict):
	h: int
	s: int
	l: int


class _HSLAColor(TypedDict):
	h: int
	s: int
	l: int
	a: float


class _HEXColor(TypedDict):
	hex: str


class _CSSNamedColor(TypedDict):
	name: str


RGBColor = Union[_RGBColor, tuple[int, int, int]]
RGBAColor = Union[_RGBAColor, tuple[int, int, int, float]]
HSLColor = Union[_HSLColor, tuple[int, int, int]]
HSLAColor = Union[_HSLAColor, tuple[int, int, int, float]]
HEXColor = Union[_HEXColor, str]
CSSNamedColor = Union[_CSSNamedColor, str]
