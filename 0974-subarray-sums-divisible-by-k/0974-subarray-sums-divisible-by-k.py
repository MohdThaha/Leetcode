class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        mp = {0:1}
        count = 0
        psum = 0

        for i in nums:
            psum += i
            rem = psum % k

            if rem < 0:
                rem += k
            
            if rem in mp:
               count += mp[rem]

            mp[rem] = mp.get(rem,0) + 1

        return count