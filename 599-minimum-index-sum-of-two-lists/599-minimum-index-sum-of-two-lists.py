class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        alf = defaultdict(int)
        for i in range(len(list2)):
            alf[list2[i]] = i
        ans = []
        minn = float("inf")
        for i, word in enumerate(list1):
            if word in alf:
                if alf[word] + i < minn:
                    minn = alf[word] + i
                    ans = []
                if alf[word] + i == minn:
                    ans.append(word)
        return ans