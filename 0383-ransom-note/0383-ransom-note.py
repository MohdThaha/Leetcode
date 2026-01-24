from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for ch in ransom:
            if ransom[ch] > mag[ch]:
                return False
        return True
