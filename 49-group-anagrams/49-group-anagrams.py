class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        string_map = collections.defaultdict(list)
        
        for string in strs:
            string_list = sorted(list(string))
            sorted_string = "".join(string_list)
            string_map[sorted_string].append(string)
        
        result = []
        for key in string_map:
            result.append(string_map[key])
        
        return result