from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = Counter(s)

        for i,j in enumerate(s):
            if mp[j] == 1:
                return i
        return -1