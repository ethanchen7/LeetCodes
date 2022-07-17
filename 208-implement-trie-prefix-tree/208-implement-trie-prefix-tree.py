class Trie:

    def __init__(self):
        self.word = collections.defaultdict()
        

    def insert(self, word: str) -> None:
        self.word[word] = True

    def search(self, word: str) -> bool:
        return word in self.word.keys()

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for word in self.word.keys():
            if word[0:n] == prefix:
                return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)