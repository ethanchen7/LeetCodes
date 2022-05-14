class Solution:
    def numTrees(self, n: int) -> int:
        
        numTrees = [1] * (n + 1)
        
        # numTrees[0] = 1
        # numTrees[1] = 1
        
        for nodes in range(2, n + 1):
            count = 0
            for root in range(1, nodes + 1):
                # find the index of numTrees cache to reference
                left = root - 1
                right = nodes - root
                count += numTrees[left] * numTrees[right]
            
            numTrees[nodes] = count
        
        return numTrees[n]
            