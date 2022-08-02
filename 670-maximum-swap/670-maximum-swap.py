class Solution:
    def maximumSwap(self, num: int) -> int:
        
        list_num = list(str(num))
        max_idx = len(list_num) - 1
        
        x, y = 0, 0
        for i in range(len(list_num)- 1, -1, -1):
            
            if list_num[i] > list_num[max_idx]:
                max_idx = i
            
            elif list_num[i] < list_num[max_idx]:
                x = i
                y = max_idx
        
        list_num[x], list_num[y] = list_num[y], list_num[x]
        return int("".join(list_num))