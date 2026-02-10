class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        mp = {}

        for i in range(len(list1)):
            mp[list1[i]] = i

        minval = float('inf')
        res = []

        for j in range(len(list2)):
            if list2[j] in mp:
                idxsum = j + mp[list2[j]]

                if idxsum < minval:
                    minval = idxsum
                    res = [list2[j]]       
                elif idxsum == minval:
                    res.append(list2[j])  
        return res
