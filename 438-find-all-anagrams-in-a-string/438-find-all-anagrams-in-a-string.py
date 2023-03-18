class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alf = defaultdict(int)
        for char in p:
            alf[char] += 1
        answer = []
        for i, char in enumerate(s):
            alf[char] -= 1
            if alf[char] == 0:
                del alf[char]
            if i >= len(p):
                last_char = s[i - len(p)]
                alf[last_char] += 1
                if alf[last_char] == 0:
                    del alf[last_char]
            if len(alf) == 0:
                answer.append(i - len(p) + 1)
        return answer

        