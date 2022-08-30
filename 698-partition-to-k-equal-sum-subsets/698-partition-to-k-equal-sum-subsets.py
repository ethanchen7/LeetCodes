class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        s = sum(nums)
        if s % k != 0:
            return False
        
        nums.sort(reverse=True)
        target_sum = s // k
        
        if nums[0] > target_sum:
            return False
        
        used = [False] * len(nums)
        
        memo = {}
        def backtrack(idx, k, subset_sum):
            
            if k == 0: # we finished finding all k pairs, return True
                return True
            
            if subset_sum == target_sum:
                return backtrack(0, k - 1, 0) # we found one, decrement k and keep going
            
            for j in range(idx, len(nums)):
                # the last condition is to check for duplicate numbers, we can skip those
                if used[j] or subset_sum + nums[j] > target_sum or (j > 0 and nums[j] == nums[j-1] and not used[j-1]):
                    continue
                
                used[j] = True
                if backtrack(j + 1, k, subset_sum + nums[j]):
                    return True
                used[j] = False
            
            return False
        
        return backtrack(0, k, 0)