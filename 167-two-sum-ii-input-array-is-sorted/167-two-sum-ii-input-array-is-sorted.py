class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(numbers) - 1
        
        while low < high:
            
            current_sum = numbers[low] + numbers[high]
            
            if current_sum < target:
                low += 1
            
            elif current_sum > target:
                high -= 1
            
            else:
                return [low + 1, high + 1]