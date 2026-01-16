class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = {}

        for i,v in enumerate(nums):
            if v not in n:
                n[v]=i
            else:
                if abs(i - n[v]) <= k:
                    return True
                n[v] = i
        return False

        