class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        arr = []
        for row in mat:
            for val in row:
                arr.append(val)

        res = []
        idx = 0
        for _ in range(r):
            res.append(arr[idx:idx + c])
            idx += c

        return res
