# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []
        
        for head in lists:
            curr = head
            
            while curr:
                heappush(minHeap, curr.val)
                curr = curr.next
        
        result = ListNode()
        tail = result
        while minHeap:
            val = heappop(minHeap)
            result.next = ListNode(val)
            result = result.next
        
        return tail.next