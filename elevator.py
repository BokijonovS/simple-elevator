class Elevator:
    def __init__(self, floors=10):
        self.current_floor = 1
        self.floors = floors

    def go_to_floor(self, target_floor):
        if target_floor < 1 or target_floor > self.floors:
            print("Invalid floor selection.")
            return

        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Going up... Floor {self.current_floor}")

        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Going down... Floor {self.current_floor}")

        print(f"Arrived at floor {self.current_floor}!")


def main():
    elevator = Elevator(floors=10)
    while True:
        try:
            target = int(input("Enter the floor number (1-10, or 0 to exit): "))
            if target == 0:
                print("Exiting elevator system.")
                break
            elevator.go_to_floor(target)
        except ValueError:
            print("Please enter a valid floor number.")


if __name__ == "__main__":
    main()
