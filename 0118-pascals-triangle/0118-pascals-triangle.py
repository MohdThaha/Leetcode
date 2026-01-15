class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []
        
        for i in range (numRows):
            current  = []
            for j in range(i + 1):

                if j == 0 or j == i:
                    current.append(1)
                else:
                    current.append(result[i-1][j-1]+result[i-1][j])
            result.append(current)
        return result