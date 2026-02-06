class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        res = []

        for i in image:
            i.reverse()
            res.append(i)

        for i in range(len(res)):
            for j in range(len(res[i])):
                if res[i][j] == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = 0

        return res
        