class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        
        self.root = TrieNode()


        

    def insert(self, word: str) -> None:
        
        level = self.root

        for c in word:
            if c not in level.children:
                # go down to next level
                level.children[c] = TrieNode()
            
            level = level.children[c]
        
        level.endOfWord = True


    def search(self, word: str) -> bool:
        level = self.root
        for c in word:
            if c not in level.children:
                return False            
            level = level.children[c]
        if level.endOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        
        level = self.root
        for c in prefix:
            if c not in level.children:
                return False            
            level = level.children[c]
        return True


        
        