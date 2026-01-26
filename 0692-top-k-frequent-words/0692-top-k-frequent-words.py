class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = Counter(words)
        word_sort = sorted( mp, key=lambda w: (-mp[w],w))
        return word_sort[:k]         