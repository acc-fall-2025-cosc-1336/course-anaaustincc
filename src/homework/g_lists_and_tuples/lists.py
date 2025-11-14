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


def get_p_distance(list1: List[str], list2: List[str]) -> float:
	"""Return the p-distance between two equal-length lists.

	The p-distance is the proportion of positions that differ between the two
	lists. Both lists must have the same non-zero length. Implementation uses
	explicit loops and indexed access only.
	"""
	if list1 is None or list2 is None:
		raise ValueError("Input lists must be non-None")

	len1 = len(list1)
	len2 = len(list2)
	if len1 != len2:
		raise ValueError("Lists must have the same length to compute p-distance")
	if len1 == 0:
		raise ValueError("Lists must have positive length")

	mismatches = 0
	i = 0
	while i < len1:
		if list1[i] != list2[i]:
			mismatches += 1
		i += 1

	# return proportion
	return mismatches / float(len1)


def get_p_distance_matrix(list_of_lists: List[List[str]]) -> List[List[float]]:
	"""Compute the p-distance matrix for a collection of equal-length lists.

	Returns an n x n matrix D where D[i][j] = p-distance(list_of_lists[i], list_of_lists[j]).
	"""
	if list_of_lists is None:
		raise ValueError("Input must be a non-None list of lists")

	n = len(list_of_lists)
	# initialize n x n matrix with zeros
	D: List[List[float]] = []
	i = 0
	while i < n:
		row: List[float] = []
		j = 0
		while j < n:
			row.append(0.0)
			j += 1
		D.append(row)
		i += 1

	# fill upper triangle using get_p_distance and mirror
	i = 0
	while i < n:
		j = i + 1
		while j < n:
			# use get_p_distance for pairwise distance
			d = get_p_distance(list_of_lists[i], list_of_lists[j])
			D[i][j] = d
			D[j][i] = d
			j += 1
		i += 1

	return D
