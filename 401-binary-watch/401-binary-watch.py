class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        self.answer = []
        self.dfs(turnedOn, [])
        return self.answer
    def dfs(self, k, now):
        if k < 0:
            return
        if len(now) == 10:
            hours = self.chet(now, 0, 4)
            minutes = self.chet(now, 4, len(now))
            if 0 <= hours <= 11 and 0 <= minutes <= 59 and k == 0:
                self.answer.append(str(hours) + ":" + "0" * int(minutes < 10) + str(minutes))
            return
        now.append(0)
        self.dfs(k, now)
        now.pop()
        now.append(1)
        self.dfs(k - 1, now)
        now.pop()
    
    def chet(self, now, st, end):
        answer = 0
        k = 1
        for i in range(st, end):
            answer = answer * 2 + now[i]
        return answer