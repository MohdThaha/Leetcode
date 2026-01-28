class NumArray:

    def __init__(self, nums: List[int]):
        self.val = nums
    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(len(self.val)):
            if left <= i <= right:
                sum += self.val[i]
        return sum 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)