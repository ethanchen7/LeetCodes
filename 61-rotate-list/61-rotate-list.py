# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []
        
        if not head:
            return None
        
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        self.rotate_arr(nums, k)
        
        curr = head
        i = 0
        while curr:
            curr.val = nums[i]
            curr = curr.next
            i += 1
        
        return head
        
    def rotate_arr(self, nums, k):
        if k == 0:
            return
        
        nums.reverse()
        
        K = k % len(nums)

        left = 0
        right = K - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = K
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
