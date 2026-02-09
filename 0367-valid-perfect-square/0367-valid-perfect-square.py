class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0,num

        if num == 1:
            return True

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
        