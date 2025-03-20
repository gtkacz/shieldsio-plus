from typing import TypeAlias, Union

from src.common.enums import ShieldsIONamedColors
from src.common.types import HexCode

ShieldsIOColor = Union[ShieldsIONamedColors, HexCode]
