# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get to the middle, reverse the end 
        
        if not head:
            return
        
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        curr = head
        while curr != prev and prev is not None:
            temp = curr.next
            curr.next = prev
            if prev == temp:
                break
            tmpPrev = prev.next
            prev.next = temp
            prev = tmpPrev
            curr = temp
        
        return head