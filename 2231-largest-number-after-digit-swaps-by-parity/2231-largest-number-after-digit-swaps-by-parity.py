class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        num_str = str(num)
        while num > 0:
            if num % 2 == 0:
                even.append(num%10)
            else:
                odd.append(num%10)
            num//= 10
        even.sort()
        odd.sort()
        ans = 0
        for i in range(len(num_str)):
            if int(num_str[i]) % 2 == 0:
                ans = ans * 10 + even.pop()
            else:
                ans = ans * 10 + odd.pop()
        return ans