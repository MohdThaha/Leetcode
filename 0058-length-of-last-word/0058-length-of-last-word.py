class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.split(" ")
        
        for i in range(len(res)-1,-1,-1):
            if res[i] != "":
                return len(res[i])
