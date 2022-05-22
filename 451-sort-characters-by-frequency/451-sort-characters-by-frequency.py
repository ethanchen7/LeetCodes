from heapq import *
class Solution:
    def frequencySort(self, s: str) -> str:
        
        maxHeap = []
        char_frequency = {}
        for char in s:
            if char not in char_frequency:
                char_frequency[char] = 0
            
            char_frequency[char] += 1
        
        for c in char_frequency:
            heappush(maxHeap, [-char_frequency[c], c])
        
        res = ""
        while len(maxHeap) > 0:
            freq, char = heappop(maxHeap)
            res += char * abs(freq)
        
        return res