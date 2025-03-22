from typing import Union

from src.common.enums import ShieldsIONamedColor
from src.common.types.hex_code import HexColor

ShieldsIOColor = Union[ShieldsIONamedColor, HexColor]
