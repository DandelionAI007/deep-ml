def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
    a_row, a_col = len(a), len(a[0])
    b_row, b_col = len(b), len(b[0])
    if a_col != b_row:
        return -1
        
    c_row, c_col = a_row, b_col
    c= []
    for i in range(c_row):
        row_res = []
        for j in range(c_col):
            a_row_i = a[i]
            b_col_j = [b[x][j] for x in range(b_row)]

            res = sum(a_ele * b_ele for a_ele, b_ele in zip(a_row_i, b_col_j))
            row_res.append(res)
        c.append(row_res)
    
    return c
