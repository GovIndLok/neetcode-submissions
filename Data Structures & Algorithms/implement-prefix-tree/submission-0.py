class PrefixTree:

    def __init__(self):
        self.ChildRef = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        currNode = self
        for i in word:
            if i not in currNode.ChildRef:
                currNode.ChildRef[i] = PrefixTree()
            currNode = currNode.ChildRef[i]
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        currNode = self
        for i in word:
            if i not in currNode.ChildRef:
                return False
            currNode = currNode.ChildRef[i]
        
        return True if currNode.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        currNode = self
        for i in prefix:
            if i not in currNode.ChildRef:
                return False
            currNode = currNode.ChildRef[i]
        
        return True