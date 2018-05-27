class Elevator:
    def __init__(self, currentFloor, doorStatus,  minFloor, maxFloor):
        self.currentFloor = currentFloor
        self.doorStatus = doorStatus
        self.maxFloor= maxFloor
        self.minFloor= minFloor

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
        if requestedFloor <= self.maxFloor and requestedFloor>=self.minFloor:
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

main()
    