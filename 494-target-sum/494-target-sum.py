class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = sum(nums)
        
        self.memo = collections.defaultdict(int)
        
        def calculate(idx, total):
            
            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if (idx, total) in self.memo:
                return self.memo[(idx, total)]
            
            add = calculate(idx + 1, total + nums[idx])
            subtract = calculate(idx + 1, total - nums[idx])
            
            self.memo[(idx, total)] = add + subtract
            return self.memo[(idx, total)]
        
        return calculate(0, 0)
        