class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        i = 0
        j = 0 
        start = 0

        while i < len(haystack): 
            if haystack[i] == needle[j]:
                if j == 0:
                    start = i
                i += 1
                j += 1
                if j == len(needle):
                    return start
            else:
                if j > 0:
                    i = start + 1
                    j = 0
                else:
                    i += 1
        return - 1
   
            

        