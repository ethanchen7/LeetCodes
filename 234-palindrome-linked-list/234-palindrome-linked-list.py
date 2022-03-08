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
        
        # slow and fast, get to the middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # slow is at the middle
        prev = None
        while slow:
            
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        while prev and head:
            
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next
        
        return True
       