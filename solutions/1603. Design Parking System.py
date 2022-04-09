class ParkingSystem:
​
    def __init__(self, big: int, medium: int, small: int):
        self.record = [big, medium, small]
    
    def addCar(self, carType: int) -> bool:
        # carType -= 1
        # if self.record[carType] > 0 :
        #     self.record[carType] -= 1
        #     return True
        # return False
        
        #two-liners by lee215
        self.record[carType - 1] -= 1
        return self.record[carType - 1] >= 0
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
