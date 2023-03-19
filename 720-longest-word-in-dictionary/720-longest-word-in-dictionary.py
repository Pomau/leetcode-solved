class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_sort = [[] for _ in range(max([len(i) for i in words]))]
        for word in words:
            words_sort[len(word) - 1].append(word)
        words_maxn = {""}
        answer = ""
        for i in range(len(words_sort)):
            words_now = set()
            for word in words_sort[i]:
                if word[:-1] in words_maxn:
                    words_now.add(word)
                    if answer > word or len(answer) < len(word):
                        answer = word
            words_maxn = words_now
        return answer
            
            
            
        
        