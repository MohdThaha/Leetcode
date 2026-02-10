class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []

        counter = Counter(nums)

        for i,j in counter.most_common(k):
            res.append(i)
        return res
        