class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=self.order)
        return arr
    def order(self, elem):
        return [str(bin(elem)).count("1"), elem]