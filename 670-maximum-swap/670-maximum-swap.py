class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_list = list(str(num))
        max_idx = len(num_list) - 1
        
        low, high = 0, 0
        
        for i in range(len(num_list) - 1, -1, -1):
            
            if num_list[i] > num_list[max_idx]:
                max_idx = i
            
            elif num_list[i] < num_list[max_idx]:
                low = i
                high = max_idx
        
        num_list[low], num_list[high] = num_list[high], num_list[low]
        return "".join(num_list)