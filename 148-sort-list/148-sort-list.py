# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def split(head):
            
            if not head or not head.next:
                return head
            
            slow, fast = head, head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            right = slow.next
            slow.next = None
            
            left = split(head)
            right = split(right)
            return merge(left, right)
        
        def merge(left, right):
            
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
        
        return split(head)