from enum import Enum, EnumMeta, IntEnum, StrEnum
from typing import List


class __MetaEnum(EnumMeta):
	"""
	Metaclass for `BetterEnum`. Adds `names` and `values` properties to the enum.
	"""

	@property
	def names(cls) -> List[str]:
		"""
		Returns the names of the enum.

		Returns:
			List[str]: Names of the enum.
		"""
		return cls._member_names_

	@property
	def values(cls) -> List[str]:
		"""
		Returns the values of the enum.

		Returns:
			List[str]: Values of the enum.
		"""
		return list(map(lambda x: x.value, cls._member_map_.values()))


class BetterEnum(Enum, metaclass=__MetaEnum):
	"""
	BetterEnum is an `enum.Enum` subclass that allows to add a prefix to all the values of the enum.
	Also adds `names` and `values` properties to the enum.

	Args:
		prefix (str, optional): Prefix to add to all the values of the enum. Defaults to "".
	"""


class BetterIntEnum(IntEnum, metaclass=__MetaEnum):
	"""
	BetterIntEnum is an `enum.IntEnum` subclass that allows to add a prefix to all the values of the enum.
	Also adds `names` and `values` properties to the enum.

	Args:
		prefix (str, optional): Prefix to add to all the values of the enum. Defaults to "".
	"""


class BetterStrEnum(StrEnum, metaclass=__MetaEnum):
	"""
	BetterIntEnum is an `enum.StrEnum` subclass that allows to add a prefix to all the values of the enum.
	Also adds `names` and `values` properties to the enum.

	Args:
		prefix (str, optional): Prefix to add to all the values of the enum. Defaults to "".
	"""
