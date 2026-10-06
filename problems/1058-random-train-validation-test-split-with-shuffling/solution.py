import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n_samples = data.shape[0]

    idxs = np.random.default_rng(seed).permutation(n_samples)

    train_end = int(n_samples * train_frac)
    val_end = train_end + int(n_samples * validation_frac)

    train_split = data[idxs[:train_end]]
    val_split = data[idxs[train_end:val_end]]
    test_split = data[idxs[val_end:]]

    return [train_split, val_split, test_split]
    
