from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        char_frequency = {}
        for char in s:
            if char not in char_frequency:
                char_frequency[char] = 0
            char_frequency[char] += 1
        
        maxHeap = []
        for c in char_frequency:
            heappush(maxHeap, [-char_frequency[c], c])
        
        res = ""
        prevFreq, prevChar = None, 0
        while maxHeap:
            freq, char = heappop(maxHeap)
            
            if prevChar and prevFreq < 0:
                heappush(maxHeap, [prevFreq, prevChar])

            res += char
            freq += 1
            prevFreq, prevChar = freq, char
                
        if len(res) == len(s):
            return res
        return ""