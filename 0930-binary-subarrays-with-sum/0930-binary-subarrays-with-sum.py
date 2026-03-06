class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = 0
        presum = 0
        freq =  {0: 1}  

        for i in nums:
            presum += i

            r = presum -goal
            if r in freq:
                count += freq[r]

            freq[presum] = freq.get(presum,0)+1
        return count 