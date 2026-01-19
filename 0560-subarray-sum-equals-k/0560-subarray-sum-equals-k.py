class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0 
        psum = 0
        x = {0:1}

        for i in nums:
            psum += i

            if psum - k in x:
                count += x[psum - k] 

            x[psum] = x.get(psum,0)+1

        return count
            


        