from typing import Union

from src.common.enums import ShieldsIONamedColors
from src.common.types.hex_code import HexCode

ShieldsIOColor = Union[ShieldsIONamedColors, HexCode]
