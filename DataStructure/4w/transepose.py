def transpose_mat(mat):
    rows = len(mat)
    cols = len(mat[0])

    ret_mat = [[0] * rows for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            ret_mat[col][row] = mat[row][col]

    return ret_mat

data = [
    [15, 0, 0, 22, 0, -15],
    [0, 11, 3, 0, 0, 0],
    [0, 0, 0, -6, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [91, 0, 0, 0, 0, 0],
    [0, 0, 28, 0, 0, 0],
]
print("sparse matrix >>")
print(transpose_mat(data))