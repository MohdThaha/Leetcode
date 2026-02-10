class Solution:
    def findLHS(self, nums: List[int]) -> int:

        mp = Counter(nums)

        res = 0

        for i,j in mp.items():
            reminder = i-1

            if reminder in mp:
                length = mp[reminder]  + j
                res = max(res , length)  
        
        return res