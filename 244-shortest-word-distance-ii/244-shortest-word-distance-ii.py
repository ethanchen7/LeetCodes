class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = {}
        for i, word in enumerate(wordsDict):
            if word not in self.locations:
                self.locations[word] = []
            self.locations[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        
        location1 = self.locations[word1]
        location2 = self.locations[word2]
        l1, l2 = 0, 0
        
        min_distance = math.inf
        while l1 < len(location1) and l2 < len(location2):
            min_distance = min(min_distance, abs(location1[l1] - location2[l2]))
        
            if location1[l1] < location2[l2]:
                l1 += 1
            else:
                l2 += 1
        
        return min_distance
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)