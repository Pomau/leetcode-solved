class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        now_m = int(current[:2]) * 60  + int(current[3:])
        tar_m = int(correct[:2]) * 60  + int(correct[3:])
        end = 24 * 60
        if tar_m >= now_m:
            return self.find(now_m, tar_m)
        return self.find(now_m, end+ tar_m)
    def find(self, st, end):
        ans = 0
        while st != end:
            ans += 1
            if st + 60 <= end:
                st += 60
            elif st + 15 <= end:
                st += 15
            elif st + 5 <= end:
                st += 5
            elif st + 1 <= end:
                st += 1
        return ans