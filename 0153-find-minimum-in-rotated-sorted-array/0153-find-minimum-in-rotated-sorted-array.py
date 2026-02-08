class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = nums[0]

        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] <= nums[r]:
                minval = min(minval, nums[l])
                break

            mid = (l + r) // 2
            minval = min(minval, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid

        return min(minval, nums[l])   # 👈 critical line
