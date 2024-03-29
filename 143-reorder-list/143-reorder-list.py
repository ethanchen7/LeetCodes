# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
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
        
        curr = head
        while curr and prev:
            tempCurr = curr.next
            curr.next = prev
            tempPrev = prev.next
            prev.next = tempCurr
            curr = tempCurr
            prev = tempPrev
        
        if curr: curr.next = None
        return head