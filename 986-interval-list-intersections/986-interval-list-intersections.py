class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        # add the max start, min end of each overlapping interval
        a, b = 0, 0
        
        res = []
        
        while a < len(firstList) and b < len(secondList):
            
            a_overlaps_b = firstList[a][1] >= secondList[b][0] and firstList[a][0] <= secondList[b][0]
            
            b_overlaps_a = secondList[b][0] <= firstList[a][0] and secondList[b][1] >= firstList[a][0]
                
            if a_overlaps_b or b_overlaps_a:
                new_interval = [max(firstList[a][0], secondList[b][0]),
                                min(firstList[a][1], secondList[b][1])]
                
                res.append(new_interval)
            
            if firstList[a][1] < secondList[b][1]:
                a += 1
            
            else:
                b += 1
                
        return res