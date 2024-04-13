class Car:
    nums_wheel = 4

    def __init__(self, color):
        self.wheels = Car.nums_wheel
        self.color = color

    def drive(self):
        if self.wheels < Car.nums_wheel:
            return self.color + " car can't drive!"
        return self.color + " car goes vroom!"

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1
