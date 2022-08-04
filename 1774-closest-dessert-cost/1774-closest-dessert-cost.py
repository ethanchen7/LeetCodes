class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        # run a dfs/backtrack bruteforce to find all combinations with each starting base
        
        # decisions
        # take 0 1 or 2 of each topping
        
        dp = [[-1 for i in range((sum(baseCosts) + sum(toppingCosts) * 2 + 1))] for i in range(len(toppingCosts))]
        
        closest = math.inf
        min_difference = math.inf
        
        def dfs(i, curr_cost):
            nonlocal closest
            nonlocal min_difference
            
            if abs(curr_cost - target) < min_difference:
                min_difference = abs(curr_cost - target)
                closest = curr_cost
            
            elif abs(curr_cost - target) == min_difference:
                closest = min(closest, curr_cost)
                
            if i == len(toppingCosts):
                return
            
            if dp[i][curr_cost] != -1:
                return dp[i][curr_cost]
            
            dfs(i + 1, curr_cost)
            dfs(i + 1, curr_cost + toppingCosts[i])
            dfs(i + 1, curr_cost + toppingCosts[i] * 2)
            
            dp[i][curr_cost] = closest
            return dp[i][curr_cost]
            # for j in range(3):
            #     curr_cost += toppingCosts[i] * j
            #     dfs(i + 1, curr_cost)
            #     curr_cost -= toppingCosts[i] * j
            
        for base in baseCosts:
            
            dfs(0, base)
        
        return closest