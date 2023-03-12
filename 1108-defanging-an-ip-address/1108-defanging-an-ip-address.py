class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = []
        for i in address:
            if i == ".":
                ans.append("[.]")
            else:
                ans.append(i)
        return "".join(ans)