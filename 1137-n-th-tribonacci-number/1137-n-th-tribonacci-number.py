class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0]
        for i in range(1, n + 1):
            if i  <= 2:
                arr.append(1)
            else:
                arr[0], arr[1], arr[2] = arr[1], arr[2], sum(arr)
        return arr[-1]