class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # Minimum is in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # Minimum is at mid or in left half
                r = mid

        return nums[l]
