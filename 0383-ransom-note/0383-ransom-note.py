class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        
        for i in magazine:
            mp[i] = mp.get(i,0) + 1
        
        for j in ransomNote:
            if j not in mp or mp[j] <= 0:
                return False
            mp[j] -= 1
        return True