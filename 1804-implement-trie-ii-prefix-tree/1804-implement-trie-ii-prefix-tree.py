class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.countStartsWith = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
            node.countStartsWith += 1 # count the path along the way
        
        node.count += 1 # "is finished count"

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
        
            node = node.children[char]
        
        return node.countStartsWith

    def erase(self, word: str) -> None:
        node = self.root
        
        for char in word:
            node = node.children[char]
            node.countStartsWith -= 1
        
        node.count -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)