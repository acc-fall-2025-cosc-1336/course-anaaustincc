"""List utility functions for homework: find lowest and highest values.

Implementations must use explicit loops and indexed access only (no built-in
min()/max() or sorting, and no slicing). These functions return the numeric
minimum/maximum from a non-empty list and raise ValueError for an empty list.
"""

from typing import List, Optional


def get_lowest_list_value(values: List[float]) -> float:
	"""Return the lowest numeric value from the list using a loop.

	Raises ValueError if the list is empty.
	"""
	if values is None:
		raise ValueError("values must be a non-None list")

	n = len(values)
	if n == 0:
		raise ValueError("List must contain at least one value")

	# Initialize with the first element
	lowest = values[0]
	i = 1
	while i < n:
		if values[i] < lowest:
			lowest = values[i]
		i += 1

	return lowest


def get_highest_list_value(values: List[float]) -> float:
	"""Return the highest numeric value from the list using a loop.

	Raises ValueError if the list is empty.
	"""
	if values is None:
		raise ValueError("values must be a non-None list")

	n = len(values)
	if n == 0:
		raise ValueError("List must contain at least one value")

	# Initialize with the first element
	highest = values[0]
	i = 1
	while i < n:
		if values[i] > highest:
			highest = values[i]
		i += 1

	return highest
