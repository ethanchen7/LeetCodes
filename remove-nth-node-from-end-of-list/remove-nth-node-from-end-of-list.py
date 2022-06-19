# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        current, prev = dummy, dummy
        
        while n > 0:
            current = current.next
            n -= 1
        
        while current.next:
            current = current.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next