class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        x = 0
        y = 0
        
        for i in word:
            if i.isupper():
                x += 1
            else:
                y += 1
        
        if x == len(word) or y == len(word):
            return True

        if word[0].isupper() and y == len(word) - 1:
            return True

        return False