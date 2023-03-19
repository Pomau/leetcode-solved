class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sums, ans = 0, 0
        d = [0] * k
        d[0] = 1
        for num in nums:
            ans = (ans + num) % k
            sums += d[ans]
            d[ans] += 1
        return sums
        
            
            
        