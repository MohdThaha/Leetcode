class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words.sort()
        n=len(s)
        k=len(words)
        ans=[]
        wk=len(words[0])
        width=k*wk
        def is_possible(st,w):
            curr=[]
            for i in range(0,len(st),wk):
                curr.append(st[i:i+wk])
            curr.sort()
            return w==curr
        for i in range(n-width+1):
            if is_possible(s[i:i+width],words):
                ans.append(i)
        return ans
        