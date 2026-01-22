class Solution:
    def reverseVowels(self, s: str) -> str:

        vowel = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)

        i = 0
        j = len(s) -1

        while i < j:
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in vowel:
                i += 1
            if s[j] not in vowel:
                j -= 1

        return "".join(s)
        