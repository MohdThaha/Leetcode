class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        wordLen = len(words[0])
        totalWords = len(words)
        totalLen = wordLen * totalWords
        wordCount = Counter(words)
        result = []
        
        # We need to check for each possible offset
        for i in range(wordLen):
            left = i
            currCount = defaultdict(int)
            count = 0
            
            # Move in steps of wordLen
            for right in range(i, len(s) - wordLen + 1, wordLen):
                word = s[right:right + wordLen]
                
                if word in wordCount:
                    currCount[word] += 1
                    count += 1
                    
                    # If word appears more than expected, shrink window
                    while currCount[word] > wordCount[word]:
                        leftWord = s[left:left + wordLen]
                        currCount[leftWord] -= 1
                        count -= 1
                        left += wordLen
                    
                    # If window matches totalWords, record index
                    if count == totalWords:
                        result.append(left)
                else:
                    # Reset window
                    currCount.clear()
                    count = 0
                    left = right + wordLen
        
        return result