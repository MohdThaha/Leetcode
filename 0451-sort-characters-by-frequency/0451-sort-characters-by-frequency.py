class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = []

        for ch,freq in count.most_common():
            res.append(ch*freq)
        
        return "".join(res)
