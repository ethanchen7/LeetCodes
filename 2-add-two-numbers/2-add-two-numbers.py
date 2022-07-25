# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        curr_l1, curr_l2 = l1, l2
        
        carry = 0
        while l1 and l2:
            
            val_sum = l1.val + l2.val + carry
            val = val_sum % 10
            carry = max(0, val_sum // 10)
            
            l1 = l1.next
            l2 = l2.next
            
            new_node = ListNode(val)
            dummy.next = new_node
            dummy = dummy.next
        
        while l1:
            val_sum = l1.val + carry
            val = val_sum % 10
            carry = max(0, val_sum // 10)
            
            new_node = ListNode(val)
            dummy.next = new_node
            dummy = dummy.next
            
            l1 = l1.next
        
        while l2:
            val_sum = l2.val + carry
            val = val_sum % 10
            carry = max(0, val_sum // 10)
            
            new_node = ListNode(val)
            dummy.next = new_node
            dummy = dummy.next
            
            l2 = l2.next
        
        if carry:
            new_node = ListNode(carry)
            dummy.next = new_node
            dummy = dummy.next
        
        return tail.next