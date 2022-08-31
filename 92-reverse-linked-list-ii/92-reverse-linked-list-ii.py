# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        left_node, beg_list = head, ListNode(next=head)
        right_node, end_list = head, None
        
        while left > 1 and left_node:
            left_node = left_node.next
            beg_list = beg_list.next
            left -= 1
            
        while right > 1 and right_node:
            right_node = right_node.next
            right -= 1
        
        end_list = right_node.next
        
        prev = None
        left_n_pointer = left_node
        while left_n_pointer != end_list:
            temp = left_n_pointer.next
            left_n_pointer.next = prev
            prev = left_n_pointer
            left_n_pointer = temp
        
        beg_list.next = right_node
        left_node.next = end_list
        
        return head if head != left_node else beg_list.next
        