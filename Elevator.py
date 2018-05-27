class Elevator:
    def __init__(self, currentFloor, doorStatus,  minFloor, maxFloor):
        self.maxFloor= maxFloor
        self.minFloor= minFloor
        self._check_floor(currentFloor)
        self.currentFloor = currentFloor
        self._check_door_status(doorStatus)
        self.doorStatus = doorStatus
        
    def _check_floor(self, currentFloor):
        if currentFloor > self.maxFloor or currentFloor < self.minFloor:
            raise ValueError("current floor should be between {0} and {1}".format(self.minFloor, self.maxFloor))
    def _check_door_status(self, doorStatus):
        if doorStatus!="C" and doorStatus!="O":
            raise ValueError("Invalid Value for Door Status")
    def door_open(self, doorStatus):
        self.doorStatus= "O"
    def door_close(self, doorStatus):
        self.doorStatus= "C"
    def _is_open(self):
        if self.doorStatus=="O":
            return True
        elif self.doorStatus=="C":
            return False
    def _is_close(self):
        if self.doorStatus=="C":
            return True
        elif self.doorStatus=="O":
            return False
    def traverse(self, requestedFloor):
        """
        args.
        """
        print("enter {0} , {1}".format(self.minFloor, self.maxFloor))
        self.door_close(self.doorStatus)
        self._check_floor(requestedFloor)
        if requestedFloor>= self.currentFloor:
            step = 1
        else:
            step = -1
        for item in range(self.currentFloor, requestedFloor, step):
            print("floor Number {0}".format(item))
        print("destination floor Number {0}".format(requestedFloor))
        self.currentFloor= requestedFloor

def main():
    sample_elevator = Elevator(1, "C", -4, 14)
    sample_elevator.traverse(1)
    sample_elevator.traverse(40)
    sample_elevator.traverse(-2)

#main()
    