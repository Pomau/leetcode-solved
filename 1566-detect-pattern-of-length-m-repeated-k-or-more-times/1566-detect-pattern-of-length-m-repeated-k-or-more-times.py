class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            ind = i
            count = 0
            while ind < len(arr) and arr[i-m + 1: i + 1] == arr[ind - m + 1: ind + 1]:
                count += 1
                ind += m
            if count >= k:
                return True
        return False
                