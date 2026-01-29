class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 1️⃣ Find the first index i from right such that nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2️⃣ If such index exists, find j and swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3️⃣ Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
