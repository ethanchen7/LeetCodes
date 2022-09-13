class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows = len(board)
        cols = len(board[0])
        result = []
        
        trie = {}
        for word in words:
            root = trie
            for char in word:
                if char not in root:
                    root[char] = {}
                root = root[char]
            root['WORD_KEY'] = word
        
        visited = set()
        
        def dfs(r,c,trie):
            
            visited.add((r,c))
            
            letter = board[r][c]
            currNode = trie[letter]
            if 'WORD_KEY' in currNode:
                result.append(currNode['WORD_KEY'])
                del currNode['WORD_KEY']
            
            
            for x, y in [(-1,0),(1,0),(0,1),(0,-1)]:
                newR, newC = r + x, c + y
                if newR < 0 or newR >= rows or newC < 0 or newC >= cols or (newR, newC) in visited or \
                board[newR][newC] not in currNode:
                    continue
                
                dfs(newR, newC, currNode)
            
            visited.remove((r,c))
            if not currNode:
                del trie[letter]
            
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r,c,trie)
        
        return result