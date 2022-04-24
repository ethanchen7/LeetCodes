class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        M = m - 1
        N = n - 1
        
        end = len(nums1) - 1
        while M >= 0 and N >= 0:
            
            if nums1[M] > nums2[N]:
                nums1[end] = nums1[M]
                M -= 1
            
            else:
                
                nums1[end] = nums2[N]
                N -= 1
                
            end -= 1
        
        
        while M >= 0:
            nums1[end] = nums1[M]
            M -= 1
            end -= 1
        
        while N >= 0:
            nums1[end] = nums2[N]
            N -= 1
            end -= 1
        
        return nums1
            