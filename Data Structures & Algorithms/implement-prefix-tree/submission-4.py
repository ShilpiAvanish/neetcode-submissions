class Node:
    def __init__(self, char=''):
        self.char = char
        self.availableNodes = {}
        self.lastLetter = False

class PrefixTree:

    def __init__(self):
        
        self.startNode = Node()
        

    def insert(self, word: str) -> None:
        
        node = self.startNode
        
        for c in word:
            if c not in node.availableNodes:    
                node.availableNodes[c] = Node(c)
            
            node = node.availableNodes[c]

        node.lastLetter = True


    def search(self, word: str) -> bool:

        node = self.startNode
        count = 0
        for c in word:
            count += 1
            if c not in node.availableNodes:
                return False

            node = node.availableNodes[c]
                
        return node.lastLetter
            
        

    def startsWith(self, prefix: str) -> bool:
        node = self.startNode

        for c in prefix:
            if c not in node.availableNodes:
                return False
                
            node = node.availableNodes[c]

        return True