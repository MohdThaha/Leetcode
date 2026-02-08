class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1
        ans = []
        
        while(l <= r):
            mid = numbers[l] + numbers[r]
            if mid == target:
                ans.append(l+1)
                ans.append(r+1)
                break
            elif mid > target:
                r-=1 
            elif mid < target:
                l+=1
        return ans