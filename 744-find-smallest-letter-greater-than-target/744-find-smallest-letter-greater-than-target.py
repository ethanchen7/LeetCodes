class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        
        left = 0
        right = len(letters) - 1
        
        # edge case if the target is less than the first letter
        # or if the target is greater than or equal to our last letter
        if ord(target) < ord(letters[0]) or ord(target) >= ord(letters[-1]):
            return letters[0]

        
        while left <= right:
            
            mid = (left + right) // 2
            
            if ord(letters[left]) > ord(target):
                return letters[left]
            
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            
            if ord(letters[mid]) > ord(target):
                right = mid - 1
        
        return letters[left]