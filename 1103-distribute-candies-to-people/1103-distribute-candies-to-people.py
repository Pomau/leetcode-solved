class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        l = 0
        r = candies
        while r - l > 1:
            m = (r + l) // 2
            if self.check(num_people, candies, m):
                l = m
            else:
                r = m
        arr = [0] * num_people
        k = l
        for i in range(num_people):
            now = (k - 1) * (num_people + num_people * (k - 1)) // 2 + k * (i + 1)
            if now <= candies:
                arr[i] = now
                candies -= now
        for i in range(num_people):
            if candies > 0:
                print(candies)
                if k * num_people+i+1 < candies:
                    arr[i] += k * num_people+i+1
                    candies -= k * num_people+i+1
                else:
                    arr[i] += candies
                    candies = 0
        return arr
    def check(self, people, n, k):
        for i in range(people):
            now = (k - 1) * (people + people * (k - 1)) // 2 + k * (i + 1)
            if now  <= n:
                n -= now
            else:
                return False
        return True