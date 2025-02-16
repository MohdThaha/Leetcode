class Solution:
    def reverseWords(self, s: str) -> str:

        ans =s.split()
        x = ans[::-1]
        return " ".join(x)

        