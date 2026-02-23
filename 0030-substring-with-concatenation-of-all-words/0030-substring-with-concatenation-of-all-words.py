class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        counter = Counter(words)
        window_size = len(words) * word_len
        ans = []
        for i in range(len(s) - window_size + 1):
            temp = s[i:i+window_size]
            
            lst = []
            while temp:
                lst.append(temp[:word_len])
                temp = temp[word_len:]
        
            if Counter(lst) == counter:
                ans.append(i)
        return ans