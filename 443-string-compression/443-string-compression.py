class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        l = 0
        for r in range(len(chars)):
            if r == len(chars) - 1 or chars[r] != chars[r + 1]:
                chars[l] = chars[r]
                l += 1
                if count > 1:
                    for ch in str(count):
                        chars[l] = ch
                        l += 1
                count = 1
            else:
                count += 1
        return l