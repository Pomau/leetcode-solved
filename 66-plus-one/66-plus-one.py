class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        transfer = 1
        for i in range(len(digits) - 1, -1, -1):
            nowsum = transfer + digits[i];
            digits[i] = nowsum % 10;
            transfer = nowsum // 10;
        if transfer > 0:
            digits.insert(0, transfer)
        return digits