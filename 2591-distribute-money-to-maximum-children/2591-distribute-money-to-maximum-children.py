class Solution:
    def distMoney(self, money: int, children: int) -> int:
        answer = 0
        money -= children
        ans = money // 7
        if ans == children - 1 and money % 7 == 3 or (ans == children and money % 7 != 0):
            ans -= 1
        if ans > children:
            ans = children - 1
        if ans < 0:
            return -1
        return ans