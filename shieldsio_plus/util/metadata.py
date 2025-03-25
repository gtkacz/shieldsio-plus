from configparser import ConfigParser
from contextlib import suppress
from getpass import getuser
from pathlib import Path
from time import time

from loguru import logger


def write_metadata(metadata_path: str = "./assets/data/metadata") -> None:
	"""
	Write metadata to a file.

	Args:
		metadata_path (optional): The path to the metadata file. Defaults to "./assets/data/metadata".
	"""
	user = None

	with suppress(OSError):
		user = getuser()

	metadata = ConfigParser()
	metadata.read(Path(metadata_path).resolve())

	metadata["main"]["user"] = user
	metadata["main"]["last-run"] = str(time())

	with Path(metadata_path).open("w", encoding="utf-8") as f:
		metadata.write(f)

	logger.debug(f"Metadata written to {metadata_path}")


def should_run(
	manifest_path: str = "./assets/data/manifest.json", metadata_path: str = "./assets/data/metadata",
) -> bool:
	"""
	Check if the script should run based on the last run time.

	Args:
		manifest_path (optional): The path to the manifest file. Defaults to "./assets/data/manifest".
		metadata_path (optional): The path to the metadata file. Defaults to "./assets/data/metadata".

	Returns:
		bool: True if the script should run, False otherwise.
	"""
	metadata = ConfigParser()
	metadata.read(Path(metadata_path).resolve())

	try:
		last_run = float(metadata["main"]["last-run"])
	except ValueError:
		return True

	if last_run < Path(manifest_path).stat().st_mtime:
		logger.debug("Manifest file has not been modified since last run.")
		return False

	return True
