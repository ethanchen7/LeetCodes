# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # get to the middle of the linked list
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True