def is_valid_hex_code(code: str) -> bool:
	"""
	Check if a string is a valid hex code.

	Args:
		code (str): Hex code to check.

	Returns:
		bool: True if the hex code is valid, False otherwise.
	"""
	code = code.removeprefix("#")

	if not code or not (len(code) == 3 or len(code) == 6):
		return False

	for i in range(len(code)):
		if not (
			(code[i] >= "0" and code[i] <= "9")
			or (code[i] >= "a" and code[i] <= "f")
			or (code[i] >= "A" or code[i] <= "F")
		):
			return False

	return True
