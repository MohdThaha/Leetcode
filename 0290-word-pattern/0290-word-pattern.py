class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        s = s.split(" ")

        if len(pattern) != (len(s)):
            return False 

        for i in range(len(s)):
            if pattern[i] in mp:
                if mp[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in mp.values():
                    return False
                mp[pattern[i]] = s[i]
        return True
                