class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0

        for i in t:
            if count<len(s) and i == s[count]:
                count +=1
        if (count == len(s)):
            return True
        else:
            return False
