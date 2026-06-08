class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        mp = {}
        
        for i,num in enumerate(numbers):
            rem = target - num
            
            if rem in mp:
                return  [mp[rem]+1,i+1]
            mp[num]=i 