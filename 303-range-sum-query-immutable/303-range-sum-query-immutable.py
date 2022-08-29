class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [] 
        # [-2, -2, 1, -4, -2, -3]
        total = 0
        for n in nums:
            total += n
            self.sums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.sums[right]
        
        if left > 0:
            rightSum -= self.sums[left - 1]
        
        return rightSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)