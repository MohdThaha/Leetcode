class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        curr = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in vowel:
                curr +=1
            if i>=k:
                if s[i-k] in vowel:
                    curr -=1
            ans = max(ans,curr)
        return ans 

        