class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split("-")) 
        y2, m2, d2 = map(int, date2.split("-"))
        if y1 > y2  or (y1 == y2 and (m1 > m2 or (m1 == m2 and d1 > d2))):
            y1, m1, d1, y2, m2, d2 = y2, m2, d2, y1, m1, d1
        m1 -= 1
        m2 -= 1
        ans = 0
        if y1 == y2:
            return self.get_days_year(y1, m1, d1, m2, d2)
        for y in range(y1 + 1, y2):
            ans += 365 + self.visok(y)
        ans += self.get_days_year(y2, 0, 0, m2, d2)
        ans += self.get_days_year(y1, m1, d1, 11, 31)
        return ans
            
    
    def visok(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def get_days(self, y, m):
        month = [31, 28 + self.visok(y), 31, 30, 31, 30, 31,31,30,31,30,31]
        return month[m]
    def get_days_year(self, y1, m1, d1, m2, d2):
        ans = 0
        if m1 == m2:
            ans += d2 - d1
        else:
            for i in range(m1 + 1, m2):
                ans += self.get_days(y1, i)
            ans += self.get_days(y1, m1)  - d1
            ans += d2
        return ans