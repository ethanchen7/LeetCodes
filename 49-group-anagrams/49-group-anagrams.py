class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)
        
        for s in strs:
            string = "".join(sorted(list(s)))
            anagrams[string].append(s)
        
        return [anagrams[word] for word in anagrams]