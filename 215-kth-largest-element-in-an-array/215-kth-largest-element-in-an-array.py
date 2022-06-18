from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return nlargest(k, nums)[-1]
        
#         maxHeap = []
#         for n in nums:
#             heappush(maxHeap, -n)
        
        
#         number = None
#         while k > 0:
#             number = -heappop(maxHeap)
#             k -= 1
        
#         if number is not None:
#             return number