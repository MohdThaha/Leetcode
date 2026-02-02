class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        nums1 = sorted(nums)
        mp = {}
        res = []

        for k,v in enumerate(nums1):
            if v not in mp:
                mp[v] = mp.get(v,0) + k
            
        for i in nums:
            res.append(mp[i])
        return res
            

        