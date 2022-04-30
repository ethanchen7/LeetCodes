class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        a, b = 0, 0
        result = []
        
        while a < len(firstList) and b < len(secondList):
            
            a_overlaps_b = firstList[a][1] >= secondList[b][0] and firstList[a][0] <= secondList[b][0]
            
            b_overlaps_a = firstList[a][0] >= secondList[b][0] and firstList[a][0] <= secondList[b][1]
            
            if a_overlaps_b or b_overlaps_a:
                newInterval = [max(firstList[a][0], secondList[b][0]), 
                               min(firstList[a][1], secondList[b][1])]
                result.append(newInterval)
            
            if firstList[a][1] < secondList[b][1]:
                a += 1
            
            else:
                b += 1
                
        return result