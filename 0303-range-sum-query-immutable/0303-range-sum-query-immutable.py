class NumArray:

    def __init__(self, nums: List[int]):
        self.val = [0]
        for i in nums:
            self.val.append(self.val[-1]+i)
    def sumRange(self, left: int, right: int) -> int:
        return self.val[right + 1] - self.val[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)