class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = []

        if rowIndex == 0:
            return [1]

        for i in range(rowIndex+1):
            current = []
            for j in range(i+1):
                if j == 0 or j == i:
                    current.append(1)
                else:
                    current.append( res[i-1][j-1] + res[i-1][j] )
            res.append(current)

        return res[rowIndex]