class UndergroundSystem:

    def __init__(self):
        self.ways = {}
        self.cars = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cars[id].append([stationName, t])
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.cars[id].append([stationName, t])
        t_delta = self.cars[id][-1][1] - self.cars[id][-2][1]
        stations = self.cars[id][-1][0] +  "$" +  self.cars[id][-2][0]
        if stations not in self.ways:
            self.ways[stations] = [0, 0]
        self.ways[stations][0] += t_delta
        self.ways[stations][1] += 1
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = endStation +  "$" + startStation
        return self.ways[stations][0] / self.ways[stations][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)