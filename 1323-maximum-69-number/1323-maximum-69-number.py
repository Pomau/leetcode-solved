class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = 0
        arr = list(str(num))
        os = True
        for i in arr:
            i = int(i)
            if i == 6 and os:
                os = False
                x = 9
            else:
                x =  i
            ans = ans * 10 + x
        return ans
                
        