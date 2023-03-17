class Node:
    def __init__(self):
        self.array = dict()
        
class Trie:

    def __init__(self):
        self.head = Node()
        self.endWord = "$"

    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            if char not in node.array:
                node.array[char] = Node()
            node = node.array[char]
        node.array[self.endWord] = None

    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char not in node.array:
                return False
            node = node.array[char]
        return (self.endWord in node.array)
        

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for char in prefix:
            if char not in node.array:
                return False
            node = node.array[char]
        return True
