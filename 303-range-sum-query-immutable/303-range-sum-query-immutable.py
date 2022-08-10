class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0] * len(nums)
        prefix = 0
        for i in range(0, len(nums)):
            self.sums[i] = nums[i] + prefix
            prefix += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        if left > 0:
            total += self.sums[right] - self.sums[left - 1]
        
        else:
            total += self.sums[right]
        
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)