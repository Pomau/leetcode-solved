class WordDictionary:

    def __init__(self):
        self.head = {}

    def addWord(self, word: str) -> None:
        node = self.head
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch] 
        node["$"] = True
        

    def search(self, word: str) -> bool:
        return self._search(word, 0, self.head)
    
    def _search(self, word, l, node):
        if l >= len(word):
            return ("$" in node)
        ans = False
        if word[l] == ".":
            for key, item in node.items():
                if key == "$":
                    continue
                ans = ans or self._search(word, l + 1, item)
        elif word[l] in node:
            ans = self._search(word, l + 1, node[word[l]])
        return ans


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)