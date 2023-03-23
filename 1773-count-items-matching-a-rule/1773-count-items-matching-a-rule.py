class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        types = {
            "color": 1,
            "type": 0,
            "name": 2
        }
        check = types[ruleKey]
        ans = 0
        for i in items:
            if i[check] == ruleValue:
                ans += 1
        return ans