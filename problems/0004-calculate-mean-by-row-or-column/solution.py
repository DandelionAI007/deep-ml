def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	if mode == "row":
		return [np.mean(row) for row in matrix]
	else:
		res = []
		for j in range(len(matrix[0])):
			col = [matrix[x][j] for x in range(len(matrix))]
			res.append(np.mean(col))
		return res


			