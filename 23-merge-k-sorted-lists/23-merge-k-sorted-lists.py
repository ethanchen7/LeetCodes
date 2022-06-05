# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []
        
        for root in lists:
            
            while root:
                heappush(minHeap, root.val)
                root = root.next
        
        if not minHeap:
            return None
        
        result = ListNode(heappop(minHeap))
        curr = result

        while len(minHeap):
            curr.next = ListNode(heappop(minHeap))
            curr = curr.next
        
        return result