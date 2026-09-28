def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if not a:
        return []

    rows = len(a)
    cols = len(a[0])

    res = [[a[j][i] for j in range(rows)] for i in range(cols)]

    return res
    