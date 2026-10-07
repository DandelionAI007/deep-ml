import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    n, m = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((m, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    # J = 1/m X^T (Xtehta - y)
    for i in range(iterations):
        theta -= alpha * (1 / n) * (X.T @ (X @ theta - y))
    
    return theta.flatten()


