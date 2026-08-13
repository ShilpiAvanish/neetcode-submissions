class TrieNode:
    def __init__(self):
        # Each node has children (next letters) and a flag for word end
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:
    def __init__(self):
        # Start with just a root node (empty prefix)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at root
        node = self.root
        # Walk down the word, adding nodes as needed
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Start at root
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # path breaks
            node = node.children[char]
        # Only valid if word was explicitly inserted
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Start at root
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True