# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        current, prev = head, None
        
        i = 0
        while i < (left - 1):
            prev = current
            current = current.next
            i += 1
        
        last_node_first_half = prev
        last_node_sub_list = current
        
        i = 0
        while i < (right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            i += 1
        
        if last_node_first_half is not None:
            last_node_first_half.next = prev
        else:
            head = prev
        
        
        last_node_sub_list.next = current
        return head
        
        
            