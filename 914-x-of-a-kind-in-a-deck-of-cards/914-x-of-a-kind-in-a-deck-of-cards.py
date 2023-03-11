class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        alf = defaultdict(int)
        for num in deck:
            alf[num] += 1
        k = None
        for key, item in alf.items():
            if k == None:
                k = item
            else:
                k = self.gcd(k, item)
        return k > 1
    def gcd(self, a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b