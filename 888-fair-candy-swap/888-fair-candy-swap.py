class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = 0
        bob = 0
        alf = set()
        for i, num in enumerate(aliceSizes):
            alice += num
            alf.add(num)
        for i, num in enumerate(bobSizes):
            bob += num
        for i, num in enumerate(bobSizes):
            target =  (alice + bob) // 2 - (bob - num)
            if target in alf:
                return [target, num]