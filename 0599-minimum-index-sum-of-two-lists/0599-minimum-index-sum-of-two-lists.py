class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        mp = {}

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    mp[list1[i]] = i + j

        minValue = min(mp.values())
    
        res = []

        for i,j in mp.items():
            if j== minValue:
                res.append(i)

        return res
        