# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2
        carry = 0
        prevNode = ListNode()
        tail = prevNode
        
        while curr1 and curr2:
            
            total = curr1.val + curr2.val + carry
            carry = total // 10
            digit = total % 10
            
            new_node = ListNode(digit)
            prevNode.next = new_node
            prevNode = prevNode.next
            
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            
            total = curr1.val + carry
            carry = total // 10
            digit = total % 10
            
            new_node = ListNode(digit)
            prevNode.next = new_node
            prevNode = prevNode.next
            
            curr1 = curr1.next
        
        while curr2:
            
            total = curr2.val + carry
            carry = total // 10
            digit = total % 10
            
            new_node = ListNode(digit)
            prevNode.next = new_node
            prevNode = prevNode.next
            
            curr2 = curr2.next
            
        if carry:
            prevNode.next = ListNode(carry)
            
        return tail.next