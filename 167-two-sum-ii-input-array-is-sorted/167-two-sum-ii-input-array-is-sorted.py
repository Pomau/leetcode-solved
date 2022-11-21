class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[r] + numbers[l] != target:
            if numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]
                