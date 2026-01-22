class Solution:
    def minimumPairRemoval(self, nums):
        res = 0

        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i-1] > arr[i]:
                    return False
            return True

        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums[idx] += nums[idx + 1]
            nums.pop(idx + 1)
            res += 1

        return res
