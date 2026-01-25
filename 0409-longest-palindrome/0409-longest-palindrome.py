from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq  = Counter(s)
        res = 0
        has_odd = False

        for i in freq.values():
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                has_odd = True
        if has_odd:
            res += 1
        return res


