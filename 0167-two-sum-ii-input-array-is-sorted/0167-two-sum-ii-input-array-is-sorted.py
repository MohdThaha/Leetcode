class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        x = 0
        y = len(numbers)-1
        ans = []
        
        while(x <= y):
            mid = numbers[x] + numbers[y]
            if mid == target:
                ans.append(x+1)
                ans.append(y+1)
                break
            elif mid > target:
                y-=1 
            elif mid < target:
                x+=1
        return ans