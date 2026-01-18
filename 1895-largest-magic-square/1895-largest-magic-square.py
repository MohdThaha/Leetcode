class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Row prefix sum
        rowSum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]

        # Column prefix sum
        colSum = [[0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]

        ans = 1

        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = rowSum[i][j + k] - rowSum[i][j]
                    valid = True

                    # Check rows
                    for r in range(i, i + k):
                        if rowSum[r][j + k] - rowSum[r][j] != target:
                            valid = False
                            break

                    # Check columns
                    for c in range(j, j + k):
                        if colSum[i + k][c] - colSum[i][c] != target:
                            valid = False
                            break

                    # Check diagonals
                    if valid:
                        diag1 = diag2 = 0
                        for d in range(k):
                            diag1 += grid[i + d][j + d]
                            diag2 += grid[i + d][j + k - d - 1]

                        if diag1 != target or diag2 != target:
                            valid = False

                    if valid:
                        ans = k

        return ans
