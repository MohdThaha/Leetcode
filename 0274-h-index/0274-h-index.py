class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        pcount = [0]* (n+1)
        
        for i in range(n):
            pcount[ min(n,citations[i]) ] += 1

        h = n 
        p = pcount[n]

        while p < h:
            h-=1
            p += pcount[h] 
        return h

