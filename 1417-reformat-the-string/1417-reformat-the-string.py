class Solution:
    def reformat(self, s: str) -> str:
        alf = []
        nums = []
        for ch in s:
            if ch.isalpha():
                nums.append(ch)
            else:
                alf.append(ch)
        ans = []
        while len(alf) > 0 and len(nums) > 0:
            ans.append(alf.pop())
            ans.append(nums.pop())
        if len(alf) > 0:
            ans.append(alf.pop())
        if len(nums) > 0:
            ans.insert(0, nums.pop())
        if len(alf) > 0 or len(nums) > 0:
            return ""
        return "".join(ans)