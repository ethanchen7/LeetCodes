class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = [log for log in logs if not log.split(' ')[1].isalpha()]
        letters = [log for log in logs if log.split(' ')[1].isalpha()]
        
        letters.sort(key=lambda x:(x.split(' ')[1:], x[0]))
        
        return letters + digits
        
        