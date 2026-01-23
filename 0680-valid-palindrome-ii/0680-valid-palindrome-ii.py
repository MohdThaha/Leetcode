class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        skip = 0
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            
            else:
                if skip == 1:
                    return False
                skip += 1

                # check skipping left
                l, r = i + 1, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    return True

                # check skipping right
                l, r = i, j - 1
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    return True

                return False
        
        return True
