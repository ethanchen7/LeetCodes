class Solution:
    def maximumSwap(self, num: int) -> int:
        
        list_num = list(str(num))
        res = list_num[:]
        
        for i in range(len(list_num)):
            for j in range(i + 1, len(list_num)):
                list_num[i], list_num[j] = list_num[j], list_num[i] # swap
                if list_num > res:
                    res = list_num[:] # save the result if it's greater
                list_num[i], list_num[j] = list_num[j], list_num[i] # swap back
        
        return "".join(res)
                
        