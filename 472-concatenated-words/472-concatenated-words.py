class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        # make a trie of all the words
        # loop through the words, check if they hit any 'WORD_KEY', increment a count for each they hit
            # once they complete a sub word, dfs the rest of the substring from the root of the trie
        # if they hit at least two, add to result array
#         trie = {}
#         for word in words:
#             root = trie
#             for char in word:
#                 if char not in root:
#                     root[char] = {}
                
#                 root = root[char]   
#             root['WORD_KEY'] = word
        
#         def searchTrie(word):
#             root = trie
#             for char in word:
#                 if char not in root:
#                     return False
#                 root = root[char]
            
#             return 'WORD_KEY' in root and root['WORD_KEY'] == word
        
        word_set = set(words)
        memo = {}
        def dfs(string):
            
            if string in memo:
                return memo[string]
            n = len(string)
            
            for i in range(1, n):
                prefix = string[:i]
                suffix = string[i:]
                if prefix in word_set and (suffix in word_set or dfs(suffix)):
                    memo[string]= True
                    return memo[string]
            memo[string] = False
            return memo[string]
        
        result = [word for word in words if dfs(word)]
        return result