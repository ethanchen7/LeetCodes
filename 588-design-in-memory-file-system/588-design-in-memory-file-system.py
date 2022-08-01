class FileSystem:

    def __init__(self):
        self.directory = collections.defaultdict(list)
        self.files = collections.defaultdict(str)
        

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split('/')[-1]] # only return the file's name
        
        return self.directory[path]

    def mkdir(self, path: str) -> None:
        directories = path.split('/')
        
        for i in range(1, len(directories)):
            cur = '/'.join(directories[:i]) or '/'
            
            if cur not in self.directory or directories[i] not in self.directory[cur]:
                bisect.insort(self.directory[cur], directories[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files:
            self.mkdir(filePath)
      
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]

    #Time:
    # ls -> O(N) split, N = len(path)
    # mkdir -> O(log P) * P (binary search * insert) * O(F) -> f = len(directory), P = number of items at directory[path]
    # addContent -> same as mkdir
    # readContent -> O(1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)