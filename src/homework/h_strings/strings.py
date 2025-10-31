"""Utility functions for Hamming distance and DNA reverse complement.

Requirements: implementations must use loops only and must not use string
slicing. These functions intentionally avoid using higher-level built-ins for
string manipulation so they are easy to follow for learning exercises.
"""

def get_hamming_distance(dna1: str, dna2: str) -> int:
	"""Return the Hamming distance between two equal-length strings.

	Raises ValueError if the strings have different lengths.
	Implementation uses explicit loops and indexing only (no slicing).
	"""
	if dna1 is None or dna2 is None:
		raise ValueError("Inputs must be non-None strings")

	len1 = len(dna1)
	len2 = len(dna2)
	if len1 != len2:
		raise ValueError("Strings must have the same length to compute Hamming distance")

	distance = 0
	i = 0
	while i < len1:
		if dna1[i] != dna2[i]:
			distance += 1
		i += 1

	return distance


def get_dna_complement(dna: str) -> str:
	"""Return the reverse complement of a DNA string.

	The reverse complement is produced by reversing the order of bases and
	replacing each base by its complement: A<->T and C<->G. This implementation
	uses explicit loops and indexing only (no slicing).

	Raises ValueError if dna contains characters other than A, C, G, T (case
	insensitive).
	"""
	if dna is None:
		raise ValueError("Input must be a non-None string")

	n = len(dna)
	# build result by iterating from the end to the start
	result = ""
	i = n - 1
	while i >= 0:
		ch = dna[i]
		# Handle uppercase and lowercase explicitly without using .upper()
		if ch == 'A' or ch == 'a':
			result += 'T'
		elif ch == 'T' or ch == 't':
			result += 'A'
		elif ch == 'C' or ch == 'c':
			result += 'G'
		elif ch == 'G' or ch == 'g':
			result += 'C'
		else:
			raise ValueError(f"Invalid DNA base: {ch}")

		i -= 1

	return result
