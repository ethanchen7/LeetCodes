# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None
        
        left = self.sortList(head)
        right = self.sortList(right)
        
        return self.mergeNodes(left, right)
        
    def mergeNodes(self, left, right):
        
        dummy = ListNode()
        tail = dummy
        
        while left and right:
        
            if left.val < right.val:
                dummy.next = left
                left = left.next

            else:
                dummy.next = right
                right = right.next
            
            dummy = dummy.next
        
        if left:
            dummy.next = left
        
        if right:
            dummy.next = right
        
        return tail.next