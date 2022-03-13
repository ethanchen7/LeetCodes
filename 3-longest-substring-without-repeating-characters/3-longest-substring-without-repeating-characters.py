class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        seen = {}
        left, right = 0, 0
        maxSub, currSub = 1, 1
        seen[s[left]] = True
        
        while right < len(s) - 1:
            
            right += 1
            if s[right] in seen:
                left += 1
                seen = {}
                seen[s[left]] = True
                right = left
                currSub = 1
            else:
                seen[s[right]] = True
                currSub += 1
            
            maxSub = max(maxSub, currSub)
        
        return maxSub