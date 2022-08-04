class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        # sort the array by attack ascending, and defense descending
        # this way we can just start from the back of the array, check that the defense is not smaller than the
        # max defense at any point
        
        # we have to sort by defense ascending to avoid having to check that the attack is not the same
        # ex: [2,1] [2,2] is not weak
        
        properties.sort(key=lambda x: (x[0], -x[1]))
        # print(properties)
        
        maxDefense = properties[-1][1]
        weak = 0
        for i in range(len(properties) - 1, -1, -1):
            if maxDefense > properties[i][1]:
                weak += 1
            maxDefense = max(maxDefense, properties[i][1])
        
        return weak
                