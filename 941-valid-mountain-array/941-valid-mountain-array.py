class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        status = 0
        for i, num in enumerate(arr):
            if i == 0:
                continue
            if num == arr[i - 1]:
                return False
            if num < arr[i - 1] and status == 0:
                if i == 1:
                    return False
                status = 1
            elif num > arr[i - 1] and status != 0:
                return False
        return status > 0
                
                