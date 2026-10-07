import numpy as np

def stratified_train_test_split(X, y, test_size, random_seed=None):
    """
    Split data into train and test sets while maintaining class proportions.
    
    Args:
        X: Feature matrix of shape (n_samples, n_features)
        y: Label vector of shape (n_samples,)
        test_size: Proportion of data for test set (0 < test_size < 1)
        random_seed: Random seed for reproducibility
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    np.random.seed(random_seed)

    n_samples = X.shape[0]

    classes = np.unique(y)

    train_idxs = []
    test_idxs = []
    for c in classes:
        idxs = np.nonzero(y == c)[0] # 定位该类别样本索引
        np.random.shuffle(idxs) 
        
        n_c = len(idxs)
        n_test = int(n_c * test_size)
        train_idxs.extend(idxs[:-n_test].tolist())
        test_idxs.extend(idxs[-n_test:].tolist())
    

    return X[train_idxs], X[test_idxs], y[train_idxs], y[test_idxs]


