class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 1
        count = 0
        for ch in s:
            if widths[ord(ch) - ord("a")] + count > 100:
                count = 0
                row += 1
            count += widths[ord(ch) - ord("a")]
        return [row, count]