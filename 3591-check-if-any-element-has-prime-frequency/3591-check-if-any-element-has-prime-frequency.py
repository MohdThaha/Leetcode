class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        freq = Counter(nums)
        
        def isPrime(n: int) -> bool:
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        for count in freq.values():
            if isPrime(count):
                return True

        return False