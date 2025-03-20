from typing import Union

from src.common.enums import ShieldsIONamedColors
from src.common.types.hex_code import HexColor

ShieldsIOColor = Union[ShieldsIONamedColors, HexColor]
