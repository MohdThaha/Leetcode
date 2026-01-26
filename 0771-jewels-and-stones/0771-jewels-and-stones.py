class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x = set(jewels)
        res = 0
        for i in stones:
            if i in x:
                res += 1 
        return res