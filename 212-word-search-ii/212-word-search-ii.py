class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows = len(board)
        cols = len(board[0])
        result = set()
        
        trie = {}
        for word in words:
            root = trie
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
            root['WORD_KEY'] = word
        
        visited = set()
        def dfs(r,c,t):
            
            letter = board[r][c]
            currNode = t[letter]
            if 'WORD_KEY' in currNode:
                result.add(currNode['WORD_KEY'])
                del currNode['WORD_KEY']
            
            visited.add((r,c))
            
            for i, j in [(-1,0),(1,0),(0,1),(0,-1)]:
                newR, newC = r + i, c + j
                if newR < 0 or newC < 0 or newR >= rows or newC >= cols or (newR,newC) in visited or \
                board[newR][newC] not in currNode:
                    continue
                dfs(newR, newC, currNode)
            
            visited.remove((r,c))
            if not currNode: # currNode = {} which means we popped out 'WORD_KEY'
                del t[letter] # take out that entire branch
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie: 
                    dfs(r, c, trie)
        
        return list(result)