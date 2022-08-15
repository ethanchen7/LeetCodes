class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        c = Counter(nums)
        result = 0
        
        for x in c:
            if k > 0 and x + k in c:
                result += 1
            
            elif k == 0 and c[x] > 1:
                result += 1
        
        return result