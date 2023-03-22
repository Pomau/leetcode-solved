class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k >= 0:
            sums = sum(code[1:k + 1])
        else:
            sums = sum(code[k:])
        ans = []
        for i in range(len(code)):
            ans.append(sums)
            if k >= 0:
                sums += -code[(i + 1) % len(code)] + code[(i + k + 1) % len(code)]
            else:
                sums += - code[(i + k) % len(code)] + code[i]
    
        return ans