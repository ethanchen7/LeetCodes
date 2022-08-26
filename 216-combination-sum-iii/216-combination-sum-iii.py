class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        result = []
        
        def dfs(idx, nums, total):
            
            if len(nums) == k:
                if total == n:
                    result.append(nums[:])
                    return
            
            if len(nums) > k:
                return
            
            if total > n:
                return
            
            for i in range(idx + 1, 10):
                total += i
                nums.append(i)
                dfs(i, nums, total)
                total -= i
                nums.pop()
        
        dfs(0, [], 0)

        return result