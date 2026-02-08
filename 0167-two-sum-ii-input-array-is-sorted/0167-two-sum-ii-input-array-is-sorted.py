class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        l, r = 0, len(n) - 1

        while l < r:
            s = n[l] + n[r]

            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r -= 1
            else:
                l += 1
