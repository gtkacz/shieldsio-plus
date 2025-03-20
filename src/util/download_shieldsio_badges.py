import concurrent.futures
from typing import Sequence

from src.common.types.esio_file import ESIOFile


def download_shields_io_badges(badges: Sequence[ESIOFile], path: str) -> None:
	"""
	Download shields.io badges in parallel using a ThreadPoolExecutor.

	Args:
	    badges: Sequence of ESIOFile objects
	    path: Directory path to save the badges
	"""

	def _download_single_badge(badge: ESIOFile) -> None:
		badge.to_shields_io_badge().download_shieldsio_badge(path)
		print(f"Downloaded: {badge.slug} to {path}")

	with concurrent.futures.ThreadPoolExecutor() as executor:
		executor.map(_download_single_badge, badges)
