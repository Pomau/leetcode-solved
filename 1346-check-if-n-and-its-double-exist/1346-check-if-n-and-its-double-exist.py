class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        alf = defaultdict(int)
        for num in arr:
            alf[num] += 1
        for num, count in alf.items():
            if 2 * num in alf and num != 0 or num == 0 and count > 1:
                return True
        return False