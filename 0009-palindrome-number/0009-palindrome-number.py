class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ = str(x)
        if x_[::-1] == x_:
            return True
        return False