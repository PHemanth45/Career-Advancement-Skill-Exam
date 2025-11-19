def transpose(mat):
    r = len(mat)
    c = len(mat[0])
    out = []

    for j in range(c):
        row = []
        for i in range(r):
            row.append(mat[i][j])
        out.append(row)
    return out

m = [[1, 2], [3, 4], [5, 6]]
result = transpose(m)
print(result)