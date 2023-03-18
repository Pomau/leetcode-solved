class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        alf = {}
        used = defaultdict(set)
        l = 0
        now = []
        if len(pattern) != s.count(" ") + 1:
            return False
        for r, ch in enumerate(s):
            if ch != " ":
                now.append(ch)
            if ch == " " or len(s) == r + 1:
                word = "".join(now)
                if pattern[l] not in alf:
                    alf[pattern[l]] = word
                    used[word].add(pattern[l])
                if alf[pattern[l]] != word or len(used[word]) > 1:
                    return False
                now = []
                l += 1
        return True

