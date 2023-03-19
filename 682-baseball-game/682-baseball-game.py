class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for oper in operations:
            if oper == "C":
                ans.pop()
            elif oper == "D":
                ans.append(ans[-1] * 2)
            elif oper == "+":
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(oper))
        return sum(ans)