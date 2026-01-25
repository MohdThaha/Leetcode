class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)
        x = 0
        
        for i in b:
            if x == len(a) or i !=a[x] : 
                return i
            x += 1

        