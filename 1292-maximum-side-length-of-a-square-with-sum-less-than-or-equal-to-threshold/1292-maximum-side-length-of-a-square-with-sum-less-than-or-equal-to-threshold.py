class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Prefix sum matrix
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = (
                    mat[i][j]
                    + pre[i][j + 1]
                    + pre[i + 1][j]
                    - pre[i][j]
                )

        def canMake(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    if (
                        pre[i][j]
                        - pre[i - k][j]
                        - pre[i][j - k]
                        + pre[i - k][j - k]
                        <= threshold
                    ):
                        return True
            return False

        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
