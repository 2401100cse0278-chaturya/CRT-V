from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    result = []
    r = rStart
    c = cStart
    result.append([r, c])
    steps = 1
    while len(result) < rows * cols:
        for _ in range(steps):
            c += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        for _ in range(steps):
            r += 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        steps += 1
        for _ in range(steps):
            c -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])
        for _ in range(steps):
            r -= 1
            if 0 <= r < rows and 0 <= c < cols:
                result.append([r, c])

        steps += 1
    return result
if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))