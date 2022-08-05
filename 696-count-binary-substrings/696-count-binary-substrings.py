class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # group the numbers into groups
        # ie. 00110011
        # [2, 2, 2, 2] # loop and add the minimum number of each group
        # ie. 00011 # the max we can group is 2
        # [3, 2]
        
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        
        res = 0
        for j in range(1, len(groups)):
            res += min(groups[j - 1], groups[j])
        
        return res