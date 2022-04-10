# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        current = ListNode()
        tail = current
        pointer = head
        
        while pointer:
            
            if pointer.val != val:
                current.next = pointer
                current = current.next
            
            if not pointer.next:
                current.next = None
            
            pointer = pointer.next
        
        return tail.next