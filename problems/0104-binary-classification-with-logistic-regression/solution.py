import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# Your code here
	X = np.array(X)
	weights = np.array(weights)
	
	z = X @ weights + bias
	pred = 1 / (1 + np.exp(-z))

	res = (pred >= 0.5).astype(int)

	return res

