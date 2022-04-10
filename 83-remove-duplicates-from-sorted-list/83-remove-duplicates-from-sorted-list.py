# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        pointer = current
        
        if not head:
            return head
        
        while pointer.next:
            
            pointer = pointer.next
            
            if pointer.val != current.val:
                current.next = pointer
                current = current.next
            
            if not pointer.next:
                current.next = None
        
        return head
        