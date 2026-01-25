class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        if len(p) > len(s):
            return res

        freq = [0] * 26

        for c in p:
            freq[ord(c) - 97] += 1

        left = 0
        right = 0
        need = len(p)

        while right < len(s):
            idx = ord(s[right]) - 97
            if freq[idx] > 0:
                need -= 1
            freq[idx] -= 1
            right += 1

            if need == 0:
                res.append(left)

            if right - left == len(p):
                idx = ord(s[left]) - 97
                if freq[idx] >= 0:
                    need += 1
                freq[idx] += 1
                left += 1

        return res
