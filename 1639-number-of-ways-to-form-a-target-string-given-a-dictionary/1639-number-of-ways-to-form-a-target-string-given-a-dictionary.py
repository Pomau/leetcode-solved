class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [0] * len(target)
        alf = defaultdict(list)
        for i, ch in enumerate(target):
            alf[ch].append(i)
        for i in range(len(words[0])):
            now = [dp[j] for j in range(len(target))]
            used = defaultdict(int)
            for word in words:
                ch = word[i]
                used[ch] += 1
            for ch, count in used.items():
                indexes = alf[ch]
                for val in indexes:
                    #print(val, now)
                    if val == 0:
                        now[val] += count
                    else:
                        now[val] += dp[val - 1]*count
            dp = now
            #print(now)
        return now[-1]%(10**9  + 7)
                
        