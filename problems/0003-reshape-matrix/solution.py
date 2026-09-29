import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row = len(a)
	col = len(a[0])

	new_row, new_col = new_shape

	if row * col != new_row * new_col:
		return []

	
	return np.array(a).reshape(new_shape).tolist()

	
	



