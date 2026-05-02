class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def f(n):
            if n in memo:
                return memo[n]
            if n <= 2:
                return n
            memo[n] = f(n-1) + f(n-2)
            return memo[n]

        return f(n)