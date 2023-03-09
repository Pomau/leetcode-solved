class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        pref = defaultdict(list)
        sums = 0
        for r, num in enumerate(arr):
            sums += num
            pref[sums].append(r)
        if sums % 3 != 0:
            return False
        k = sums // 3
        if sums == 0:
            if len(pref[0]) < 3:
                return False
            return True
        if k in pref and sums - k in pref and min(pref[k]) < max(pref[sums - k]):
            return True
        return False