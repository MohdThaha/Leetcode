from collections import defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        count = defaultdict(int)
        for c in p:
            count[c] += 1

        left = 0
        right = 0
        needed = len(p)
        res = []

        while right < len(s):
            if count[s[right]] > 0:
                needed -= 1
            count[s[right]] -= 1
            right += 1

            if needed == 0:
                res.append(left)

            if right - left == len(p):
                if count[s[left]] >= 0:
                    needed += 1
                count[s[left]] += 1
                left += 1

        return res
