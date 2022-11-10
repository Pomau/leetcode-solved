class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cat_fruits = defaultdict(int)
        l = 0
        max_fruit_collect = 0
        for r in range(len(fruits)):
            cat_fruits[fruits[r]] += 1
            while len(cat_fruits) > 2:
                cat_fruits[fruits[l]] -= 1
                if cat_fruits[fruits[l]] == 0:
                    del cat_fruits[fruits[l]]
                l += 1
            max_fruit_collect = max(max_fruit_collect, r - l + 1)
        return max_fruit_collect
            
        
# 1 2 2 1 3 2 -> 4
# 1 2 3 2 2 1 2 3 -> 4 