class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        year = date.split()[2]
        month = str(months.index(date.split()[1]) + 1)
        day = str(date.split()[0][:-2])
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        return f"{year}-{month}-{day}"