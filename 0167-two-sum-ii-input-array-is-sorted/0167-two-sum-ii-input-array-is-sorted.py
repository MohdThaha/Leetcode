class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        x = 0
        y = len(numbers)-1
        ans = []
        
        while(x <= y):
            if numbers[x] + numbers[y] == target:
                ans.append(x+1)
                ans.append(y+1)
                break
            elif numbers[x] + numbers[y] > target:
                y-=1 
            elif numbers[x] + numbers[y] < target:
                x+=1
        return ans