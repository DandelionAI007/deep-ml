def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	new_matrix = [[val * scalar for val in row] for row in matrix]

	return new_matrix

	