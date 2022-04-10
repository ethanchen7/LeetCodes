class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        low = 0
        high = len(letters) - 1
        
        if ord(target) < ord(letters[0]) or ord(target) >= ord(letters[-1]):
            return letters[0]
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if ord(letters[mid]) <= ord(target):
                low = mid + 1
            
            if ord(letters[mid]) > ord(target):
                high = mid - 1
                
        
        return letters[low]