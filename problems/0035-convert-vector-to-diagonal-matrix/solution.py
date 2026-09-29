import numpy as np

def make_diagonal(x):
	# Your code here
	m = n = len(x)

	new_matrix = [[x[i] if i == j else 0 for j in range(n)] for i in range(m)]

	return new_matrix
	