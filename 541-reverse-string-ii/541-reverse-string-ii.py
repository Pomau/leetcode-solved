class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        i = 0
        while i * 2 * k < len(s):
            self.rev(arr, i * 2 * k, min(2 * i * k + k - 1, len(s) - 1))
            i += 1
        return "".join(arr)
    def rev(self, arr, l, r):
        for i in range(l, (l + r) // 2 + 1):
            arr[i], arr[r - i + l] = arr[r - i + l], arr[i]