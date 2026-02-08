class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = float('inf')

        l = 0
        r = len(nums) - 1

        while l <= r:
            # If current subarray is already sorted
            if nums[l] <= nums[r]:
                minval = min(minval, nums[l])
                break

            mid = (l + r) // 2
            minval = min(minval, nums[mid])

            # Left half sorted → minimum must be in right half
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                # Right half sorted → minimum in left half (including mid)
                r = mid - 1

        return minval
