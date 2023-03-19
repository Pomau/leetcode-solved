class Solution:
    def minJumps(self, arr: List[int]) -> int:
        h = deque()
        alf = defaultdict(list)
        for r, num in enumerate(arr):
            alf[num].append(r)
        answer = [False for _ in range(len(arr))]
        h.append([0, 0])
        while len(h) > 0:
            z, ind = h.popleft()
            indexes = [ind + 1, ind - 1]
            for k in alf[arr[ind]]:
                if 0 <= k < len(arr) and not answer[k]:
                    answer[k] = True
                    h.append([z + 1, k])
            alf[arr[ind]] = []
            for k in indexes:
                if 0 <= k < len(arr) and not answer[k]:
                    answer[k] = True
                    h.append([z + 1, k])
            if ind == len(arr) - 1:
                return z