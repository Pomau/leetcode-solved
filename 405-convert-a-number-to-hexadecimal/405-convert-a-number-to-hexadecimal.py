class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        answer = []
        if num < 0:
            num = 4294967295 + num + 1
        while num > 0:
            answer.append(self.getCh(num % 16))
            num = num // 16
        answer.reverse()
        return "".join(answer)

                
    def getCh(self, ind):
        if ind < 10:
            return str(ind)
        return chr(ord("a") + ind - 10)