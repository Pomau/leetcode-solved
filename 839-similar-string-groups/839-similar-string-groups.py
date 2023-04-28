class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        words = [dict() for _ in range(len(strs))]
        for i, word in enumerate(strs):
            for j, ch in enumerate(word):
                if ch not in words[i]:
                    words[i][ch] = []
                words[i][ch].append(j)
        for i in range(len(strs)):
            for key, val in words[i].items():
                words[i][key] = tuple(val)
        g = [[] for _ in range(len(strs))]
        for i, word in enumerate(strs):
            for j, other in enumerate(strs):
                if i >= j:
                    continue
                os = 0
                for key, items in words[i].items():
                    # print(hash(items), hash(words[j][key]), items, words[j][key])
                    if hash(items) != hash(words[j][key]):
                        os += len(set(items) ^ set(words[j][key]))
                        if os > 4:
                            # print(len(set(items) ^ set(words[j][key])), items, words[j][key])
                            break
                if os <= 4:
                    g[i].append(j)
                    g[j].append(i)
        #print(g)
        self.g = g
        color = 0
        self.colors = [-1] * len(strs)
        for i in range(len(strs)):
            if self.colors[i] == -1:
                color += 1
                self.dfs(i, color)
        return color
    
    
    def dfs(self, u, color):
        if self.colors[u] != -1:
            return
        self.colors[u] = color
        for j in self.g[u]:
            self.dfs(j, color)
            
            