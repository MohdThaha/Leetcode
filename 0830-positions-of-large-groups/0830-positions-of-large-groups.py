class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        res = []
        value = s[0]
        start = 0
        end = 0

        for i, ch in enumerate(s):
            if ch == value:
                end = i
            else:
                difference = end - start + 1
                if difference >= 3:
                    res.append([start, end])

                value = ch
                start = i
                end = i

        difference = end - start + 1
        if difference >= 3:
            res.append([start, end])
            
        return res
