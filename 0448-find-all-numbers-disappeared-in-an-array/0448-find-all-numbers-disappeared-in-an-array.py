class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        mp = {}
        res = []

        for i in nums:
            mp[i] = mp.get(i,0)+1
        
        for i in range(1,len(nums)+1):
            if i not in mp:
                res.append(i)
        return res
        