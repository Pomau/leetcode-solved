class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        alf = defaultdict(int)
        for i, num in enumerate(arr):
            alf[num] += 1
            
        for i, num in enumerate(arr):
            if alf[num] == 1:
                k -= 1
                if k == 0:
                    return num
        return ""