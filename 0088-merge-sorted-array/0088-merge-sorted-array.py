class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = 0

        for i in range(m+n):
            if x < n and (i >= m + x or nums1[i] > nums2[x]):
                nums1.insert(i,nums2[x])
                nums1.pop()
                x+=1     

        