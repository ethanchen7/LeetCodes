class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        intersections = []
        
        idx1 = 0
        idx2 = 0
        
        while idx1 < len(firstList) and idx2 < len(secondList):
            
            a = firstList[idx1]
            b = secondList[idx2]
  
            
            a_overlap_b = a[0] <= b[0] and a[1] >= b[0]
            b_overlap_a = a[0] >= b[0] and a[0] <= b[1]
            
            if a_overlap_b:
                x = max(a[0],b[0])
                y = min(a[1],b[1])
                intersections.append([x,y])
            
            elif b_overlap_a:
                x = max(a[0],b[0])
                y = min(a[1],b[1])
                intersections.append([x,y])
            
            if a[1] < b[1]:
                idx1 += 1
            
            else:
                idx2 += 1
        
        return intersections