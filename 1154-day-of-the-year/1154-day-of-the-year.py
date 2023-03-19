class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]
        year = int(date.split("-")[0])
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month_days[1] += 1
        days = int(date.split("-")[2])
        for i in range(int(date.split("-")[1]) - 1):
            days += month_days[i]
        return days