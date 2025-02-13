class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        x = 0
        y = 1

        for i in nums:
            if i == 0:
                x += y
                y +=1
            else:
                y=1
        return x       