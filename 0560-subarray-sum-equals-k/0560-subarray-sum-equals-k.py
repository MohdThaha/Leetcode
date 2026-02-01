class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mp = {0:1}
        currentSum = 0
        count = 0
        
        for i in nums:
            currentSum += i
            rem  = currentSum - k

            if rem in mp:
                count += mp[rem]
            
            mp[currentSum] = mp.get(currentSum,0)+1
        return count
                 

        