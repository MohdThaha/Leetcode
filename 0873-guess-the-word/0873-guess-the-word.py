# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        def count_matches(word1: str, word2: str) -> int:
            """Returns the number of matching characters between two words."""
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        for _ in range(20):  # We are allowed at most 10 guesses
            guess_word = random.choice(words)  # Pick a random word from the list
            matches = master.guess(guess_word)  # Get feedback on how many characters match
            
            if matches == 6:
                return  # Found the secret word
            
            # Filter words that have the same number of matching characters as the guessed word
            words = [word for word in words if count_matches(word, guess_word) == matches]

      