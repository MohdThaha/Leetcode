class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res =[]
        for i in nums1:
            for j in nums2:
                if i == j and i not in res:
                    res.append(i)

        return res