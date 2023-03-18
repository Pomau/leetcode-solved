class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyword = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        for word in words:
            os = False
            now = self.getkey(keyword, word[0])
            for i in range(1, len(word)):
                if self.getkey(keyword, word[i]) != now:
                    os = True
            if not os:
                ans.append(word)
        return ans            
    def getkey(self, keys, ch):
        for i in range(len(keys)):
            if ch.lower() in keys[i]:
                return i