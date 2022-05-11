class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewel_freq = 0 
        
        jewels = [char for char in jewels]
        
        for stone in stones:
            if stone in jewels:
                jewel_freq += 1
        
        return jewel_freq
        