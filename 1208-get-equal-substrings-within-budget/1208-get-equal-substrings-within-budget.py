class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        total  = 0
        ans  = 0

        for r in range(len(s)):
            total += abs( ord(s[r]) - ord(t[r]) )
            
            while total > maxCost:
                total -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            ans = max(ans, r - l + 1)

        return ans
