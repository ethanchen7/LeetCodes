class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sums = collections.defaultdict(int)
        prefix_sums[0] = 1
        
        res = 0
        prefix = 0
        for n in nums:
            prefix += n
            if (prefix - k) in prefix_sums:
                res += prefix_sums[prefix-k]
        
            prefix_sums[prefix] += 1
            
        return res