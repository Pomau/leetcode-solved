class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        first = -1
        delete = -1
        for i in range(len(number)):
            if number[i] == digit:
                if i + 1 < len(number) and int(number[i]) < int(number[i + 1]):
                    delete = i
                    break
                last = i
        if delete == -1:
            delete = last
        return number[:delete] + number[delete + 1:]