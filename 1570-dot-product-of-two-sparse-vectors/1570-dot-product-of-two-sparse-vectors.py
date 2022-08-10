class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero_map = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nonzero_map[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for idx in self.nonzero_map:
            val = self.nonzero_map[idx]
            if idx in vec.nonzero_map:
                total += (val * vec.nonzero_map[idx])
        
        return total

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)