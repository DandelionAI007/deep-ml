import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    n_cols = data.shape[1]

    for idx in range(n_cols):
        column = data[:, idx]

        valid_mask = ~np.isnan(column) # 布尔索引
        valid_values = column[valid_mask]

        if len(valid_values) == 0:
            continue

        if strategy == "mean":
            statistic = np.mean(valid_values)
        elif strategy == "median":
            statistic = np.median(valid_values)
        elif strategy == "mode":
            vals, counts = np.unique(valid_values, return_counts=True)
            max_count = np.max(counts)

            modes = vals[counts == max_count]
            statistic = np.min(modes)
        else:
            raise ValueError()

        column[np.isnan(column)] = statistic

    return data
    
        
