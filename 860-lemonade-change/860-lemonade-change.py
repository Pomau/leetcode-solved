class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        nums = [0, 0, 0]
        os = True
        for i, bill in enumerate(bills):
            now = []
            if bill == 20:
                if nums[1] > 0:
                    now += [1, 0]
                else:
                    now += [0, 0, 0]
                nums[2] += 1
            elif bill == 10:
                now += [0]
                nums[1] += 1
            else:
                nums[0] += 1
            for i in now:
                if nums[i] <= 0:
                    os = False
                nums[i] -= 1
        return os
                