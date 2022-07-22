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
        dummy = ListNode(0, next=head)
        prev = dummy
        curr = head
        
        while n > 1:
            curr = curr.next
            n -= 1
        
        while curr.next:
            curr = curr.next
            prev = prev.next
        
        prev.next = prev.next.next
        return dummy.next