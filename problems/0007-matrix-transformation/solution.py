import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	if A.ndim != 2 or T.ndim != 2 or S.ndim != 2:
		return -1
	
	if A.shape[0] != A.shape[1] or T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
		 return -1

	if T.shape[1] != A.shape[0] or A.shape[1] != S.shape[0]:
		return -1

	det_t = np.linalg.det(T)
	det_s = np.linalg.det(S)
	if np.isclose(det_t, 0) or np.isclose(det_s, 0):
		return -1

	T_ver = np.linalg.inv(T)

	res = T_ver @ A @ S

	return res

