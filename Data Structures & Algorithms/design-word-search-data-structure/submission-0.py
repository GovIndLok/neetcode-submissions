class WordDictionary:

    def __init__(self):
        self.ChildRef = {}
        self.IsEnd = False

    def addWord(self, word: str) -> None:
        currNode = self
        for i in word:
            if i not in currNode.ChildRef:
                currNode.ChildRef[i] = WordDictionary()
            currNode = currNode.ChildRef[i]
        currNode.IsEnd = True

    def search(self, word: str) -> bool:
        currNode = self
        for i in range(len(word)):
            if word[i] not in currNode.ChildRef and word[i] != '.':
                return False
            if word[i] == '.':
                any_true = 0
                for _, childNode in currNode.ChildRef.items():
                    if childNode.search(word[i+1:]):
                        return True
                return False
                
            currNode = currNode.ChildRef[word[i]]
            
        return True if currNode.IsEnd else False