from typing import List
def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0

    return matrix
if __name__ == '__main__':
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        row = list(map(int, line.split()))
        matrix.append(row)
    print(setZeroes(matrix))