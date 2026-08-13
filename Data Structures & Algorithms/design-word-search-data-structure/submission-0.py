class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        level = self.root
        for c in word:
            if c not in level.children:
                level.children[c] = TrieNode()
            level = level.children[c]
        level.endOfWord = True
        

    def search(self, word: str) -> bool:

        def dfs(index, node):
            # doing some bfs solution every time their is a .
            level = node
            for j in range(index, len(word)):
                c = word[j]
                if c != '.':
                    if c not in level.children:
                        return False
                    level = level.children[c]
                else:
                    for child in node.children.values():
                        if dfs(index + 1, child):
                            return True
                    return False
            return level.endOfWord
        return dfs(0, self.root)











