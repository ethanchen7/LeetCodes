class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # the total sum of gas can never be less than cost
        if sum(gas) < sum(cost):
            return -1
        
        # now that we've guaranteed a solution exists, we can be greedy
        # check for the first point that total is greater than 0
        total = 0
        start = 0
        for i in range(len(gas)):
            
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        
        return start