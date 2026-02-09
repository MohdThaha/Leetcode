class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True
        
        l,r = 1,num

        while l < r:
            mid = (l+r) // 2
            midsq = mid * mid

            if midsq == num:
                return True
            
            elif midsq > num:
                r = mid
            else:
                l = mid + 1
        return False
        