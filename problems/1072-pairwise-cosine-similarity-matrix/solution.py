import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X)
    norm = np.sqrt(np.sum(X ** 2, axis=1, keepdims=True))

    safe_norm = np.where(norm == 0.0, 1.0, norm)
    X = X / safe_norm

    res = np.matmul(X, X.T)

    return np.round(res, 4).tolist()


