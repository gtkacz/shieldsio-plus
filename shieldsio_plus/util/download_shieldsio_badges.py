import concurrent.futures
from collections.abc import Sequence
from json import dump as json_dump
from operator import itemgetter
from pathlib import Path

from shieldsio_plus.common.types.shields_io_badge import ShieldsIOBadge


def download_shields_io_badges(shields: Sequence[ShieldsIOBadge], badge_path: str, json_path: str) -> None:
	"""
	Download shields.io badges in parallel using a ThreadPoolExecutor.

	Args:
		shields: Sequence of ShieldsIOBadge objects.
		badge_path: Directory path to save the badges.
		json_path: JSON file path to save the badge metadata.
	"""
	badges = []
	badge_path = str(Path(badge_path).resolve())

	def _download_single_badge(badge: ShieldsIOBadge) -> None:
		badge.download_shieldsio_badge(badge_path)

		badges.append(badge.to_dict())

	with concurrent.futures.ThreadPoolExecutor() as executor:
		futures = [executor.submit(_download_single_badge, badge) for badge in shields]

		for future in concurrent.futures.as_completed(futures):
			future.result()

	with Path(json_path).resolve().open("w") as f:
		json_dump(sorted(badges, key=itemgetter("slug")), f, indent=4)
