class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count, s2count = {}, {}
        for i in range(len(s1)):
            s1count[s1[i]] = s1count.get(s1[i],0) + 1 
            s2count[s2[i]] = s2count.get(s2[i],0) + 1 
        
        l = 0

        if s1count == s2count:
            return True
        
        for i in range(len(s1),len(s2)):
            s2count[s2[i]] = s2count.get(s2[i],0) + 1 
            l_ch = s2[l]
            s2count[l_ch] -= 1

            if s2count[l_ch] == 0:
                s2count.pop(l_ch)
            l += 1
            if s1count == s2count:
                return True
        
        return False
        