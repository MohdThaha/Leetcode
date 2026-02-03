class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for i in nums:
            length = len(str(i))
            if length%2 == 0:
                res +=1
        return res
        