class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        alf = defaultdict(int)
        for i, num in enumerate(arr):
            alf[num] += 1
        count = set()
        for key, item in alf.items():
            if item in count:
                return False
            count.add(item)
        return True