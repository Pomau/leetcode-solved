class Solution:
    def decodeString(self, s: str) -> str:
        counts = []
        strings = [""]
        status = []
        l = 0
        while l < len(s):
            while l < len(s) and s[l].isdigit():
                if len(status) == 0 or status[-1] != 0:
                    counts.append(int(s[l]))
                    strings.append("")
                    status.append(0)
                else:
                    counts[-1] = counts[-1] * 10 + int(s[l])
                l += 1
            if l < len(s) and s[l] == "[":
                status[-1] = 1
            elif l < len(s) and s[l] == "]":
                strings[-2] += strings[-1] * counts[-1]
                counts.pop()
                strings.pop()
                status.pop()
            elif l < len(s):
                strings[-1] += s[l]
            l += 1
        return strings[0]


