class ParkingSpot:
    def __init__(self, row, column, floor, type):
        self.row = row
        self.column = column
        self.floor = floor
        self.type = type
        self.vehicle = None
    
    def getSpot(self):
        return self.row, self.column, self.floor
    
    def park(self, vehicle):
        self.vehicle = vehicle
        
    def removeVehicle(self):
        self.vehicle = None
    
    def isFree(self):
        return self.vehicle == None

class Vehicle:
    def __init__(self, vehicleNumber, type, size,ticketId):
        self.vehicleNumber = vehicleNumber
        self.type = type
        self.size = size
        self.ticketId = ticketId
        
    def getVehicle(self):
        return self.vehicleNumber, self.type, self.size, self.ticketId
    
    
class ParkingFloor:
    def __init__(self, floor, spots):
        self.floor = floor
        self.spots = spots or []
        self.freeSpots = {2:[], 4:[]} # 2: bike, 4: car
        
    def getFreeSpots(self, vehicleType):
        return self.freeSpots[vehicleType]
    
    def park(self, vehicle, strategy):
        if strategy == 'lowIndexFirst':
            self.lowIndexFirst(vehicle)
        elif strategy == 'mostFreeSpotsFirst':
            self.mostFreeSpotsFirst(vehicle)
            
    def lowIndexFirst(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == None:
                spot.park(vehicle)
                return spot.getSpot()
            
    def mostFreeSpotsFirst(self, vehicle):
        for spot in self.freeSpots[vehicle.size]:
            if spot.vehicle == None:
                spot.park(vehicle)
                return spot.getSpot()
            
    def removeVehicle(self, ticketId):
        for spot in self.spots:
            if spot.vehicle and spot.vehicle.ticketId == ticketId:
                spot.removeVehicle()
                return True
        return False
    
class ParkingLot:
    def __init__(self, floors):
        self.floors: list[ParkingFloor] = floors or []
        
    def park(self, vehicleType, vehicleNumber, ticketId, strategy):
        for floor in self.floors:
            freeSpots = floor.getFreeSpots(vehicleType)
            if freeSpots:
                return floor.park(Vehicle(vehicleNumber, vehicleType, 2 if vehicleType == 2 else 4, ticketId), strategy)
        return None
    
    def removeVehicle(self, ticketId):
        for floor in self.floors:
            if floor.removeVehicle(ticketId):
                return True
        return False
    
    def searchVehicle(self, ticketId):
        for floor in self.floors:
            for spot in floor.spots:
                if spot.vehicle and spot.vehicle.ticketId == ticketId:
                    return spot.vehicle.getVehicle()
        return None
        

