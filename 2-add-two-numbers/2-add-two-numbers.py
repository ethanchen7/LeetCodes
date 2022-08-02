# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy 
        
        currl1 = l1
        currl2 = l2
        
        carry = 0
        while currl1 and currl2:

            curr_sum = currl1.val + currl2.val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            
            currl1 = currl1.next
            currl2 = currl2.next
        
        while currl1:
            
            curr_sum = currl1.val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            
            currl1 = currl1.next
        
        while currl2:
            
            curr_sum = currl2.val + carry
            digit = curr_sum % 10
            carry = curr_sum // 10
            
            new_node = ListNode(digit)
            dummy.next = new_node
            dummy = dummy.next
            
            currl2 = currl2.next
        
        if carry:
            new_node = ListNode(carry)
            dummy.next = new_node
        return tail.next
            
            