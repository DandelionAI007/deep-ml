def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	import numpy as np
	m, n = len(a), len(a[0])
	if n != len(b):
		return -1

	new_vec = [np.dot(np.array(row),np.array(b)) for row in a]

	return new_vec

