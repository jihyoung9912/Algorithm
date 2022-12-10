class Term:
    def __init__(self, row=0, col=0, value=0):
        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return f"{self.row, self.col, self.value}"

    def __repr__(self):
        return str(self)


class MatrixSparse:
    def __init__(self, rows=0, cols=0, size=0, sparse=None):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.sparse = sparse

    def build_matrix_sparse(self, mat):
        self.rows = len(mat)
        self.cols = len(mat[0])

        self.sparse = [
            Term(r, c, v)
            for r, row in enumerate(mat)
            for c, v in enumerate(row)
            if v != 0
        ]
        self.size = len(self.sparse)

    def __str__(self):
        if self.sparse is None:
            return ""
        ret = ""
        for term in self.sparse:
            ret += f"{term}\n"
        return ret

    def __repr__(self):
        return f"{self.sparse}"

    def transpose(self):
        if self.sparse is None:
            return
        sparse= [Term() for _ in range(self.size)]
        idx = 0
        for i in range(self.cols):
            for e in self.sparse:
                if e.col != i:
                    continue
                sparse[idx].row = e.col
                sparse[idx].col = e.row
                sparse[idx].value = e.value
                idx += 1
        return MatrixSparse(
            rows=self.cols,
            cols=self.rows,
            size=self.size,
            sparse=sparse,
        )

    def transpose_fast(self):
        row = [0] * self.cols
        for i in range(self.cols):
            for j in self.sparse:
                if j.col == i:
                    row[i] += 1

        print(f"Row size = {row}")

        rowstart = [0] * self.cols
        for i in range(len(rowstart) - 1):
            rowstart[i + 1] = row[i] + rowstart[i]
        print(f"Row Start = {rowstart}")

        if self.sparse is None:
            return
        sparse = [Term() for _ in range(self.size)]
        for i in self.sparse:
            sparse[row[i.col]].row = i.col
            sparse[row[i.col]].col = i.row
            sparse[row[i.col]].value = i.value
            row[i.col] += 1
        self.sparse = sparse
        return sparse


data = [
    [15, 0, 0, 22, 0, -15],
    [0, 11, 3, 0, 0, 0],
    [0, 0, 0, -6, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [91, 0, 0, 0, 0, 0],
    [0, 0, 28, 0, 0, 0],
]
print("sparse matrix >>")

mat = MatrixSparse()
mat.build_matrix_sparse(data)
print(mat)

print("fast transpose >>")
mat.transpose_fast()
print(mat)
