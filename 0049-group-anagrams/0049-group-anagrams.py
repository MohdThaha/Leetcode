class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            ans[key].append(i)
        
        return list(ans.values())
        