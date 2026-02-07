class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx  = 0

        for i in nums:
            if i == target:
                return idx
            else:
                idx +=1
        return -1
        