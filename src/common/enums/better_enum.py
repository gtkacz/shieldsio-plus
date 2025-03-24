from typing import Any

from aenum import Enum, EnumMeta, IntEnum, StrEnum


class __MetaEnum(EnumMeta):
	"""
	Metaclass for `BetterEnum`. Adds `names` and `values` properties to the enum.
	"""

	@property
	def names(cls) -> list[str]:
		"""
		Returns the names of the enum.

		Returns:
			list[str]: Names of the enum.
		"""
		return sorted(cls._member_names_)

	@property
	def values(cls) -> list[Any]:
		"""
		Returns the values of the enum.

		Returns:
			list[str]: Values of the enum.
		"""
		return list(map(lambda x: x.value, cls._member_map_.values()))

	@property
	def members(cls) -> list:
		"""
		Returns the members of the enum.

		Returns:
			dict: Members of the enum.
		"""
		return list(cls.__members__.values())


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
