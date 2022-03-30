class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        result = []
        i, j = 0, 0
        
        if not firstList or not secondList:
            return result
        
        while i < len(firstList) and j < len(secondList):
            
            first_overlaps_second = firstList[i][0] <= secondList[j][0] and firstList[i][1] >= secondList[j][0]
            
            second_overlaps_first = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            
            if first_overlaps_second or second_overlaps_first:
                result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
            
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
            
        
        return result
                
        
        
        