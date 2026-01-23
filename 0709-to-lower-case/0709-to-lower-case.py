class Solution:
    def toLowerCase(self, s: str) -> str:
        
        res = ""

        for i in s:
            val = ord(i)
            if 65 <= val <= 90:
                res += chr ( val + 32 )
            else:
                res += i
        return  res