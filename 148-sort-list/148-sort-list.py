# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next: # get to the middle
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next # start the other half of the linked list
        
        slow.next = None 
        
        left = self.sortList(head)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def merge(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        return tail.next