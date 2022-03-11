class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        people_who_trust = set()
        
        for a, b in trust:
            people_who_trust.add(a)
            
        if len(people_who_trust) == n:
            return -1
        
        
        potential_judge = None
        for i in range(1, n + 1):
            if i not in people_who_trust:
                potential_judge = i
        
        people_who_trust_judge = set()
        
        for a, b in trust:
            if b == potential_judge:
                people_who_trust_judge.add(a)
        
        if len(people_who_trust_judge) != n-1:
            return -1
        return potential_judge