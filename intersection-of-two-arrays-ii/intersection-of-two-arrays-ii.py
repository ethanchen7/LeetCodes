class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freq = Counter(nums1)
        result = []
        
        for n in nums2:
            if freq[n] > 0:
                result.append(n)
                freq[n] -= 1
            
        return result
        