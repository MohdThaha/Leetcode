class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: i for i, name in enumerate(list1)}

        min_sum = float('inf')
        res = []

        for j, name in enumerate(list2):
            if name in index_map:
                s = index_map[name] + j
                if s < min_sum:
                    min_sum = s
                    res = [name]
                elif s == min_sum:
                    res.append(name)

        return res
