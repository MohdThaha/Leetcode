class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = secound = third = None

        for i in nums:
            if i == first or i==secound or i == third:
                continue

            if third is None or third < i:
                first = secound
                secound = third
                third = i
            elif secound is None or secound< i:
                first = secound
                secound = i
            elif first is None or first< i: 
                first = i

        return first if first is not None else third