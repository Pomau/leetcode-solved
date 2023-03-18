class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        answer = 0
        dx = [-1, 1]
        for i in nums:
            count_el = 1
            for k in range(2):
                el = i + dx[k]
                while el in numbers:
                    numbers.remove(el)
                    el += dx[k]
                    count_el += 1
            answer = max(answer, count_el)
        return answer
            
                
        
        