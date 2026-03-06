class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        n = len(s)
        res = n
        left = 0

        for right in range(n):
            count[s[right]] -= 1

            while left < n and all(count[c] <= n//4 for c in "QWER"):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1

        return res