class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = Point(3,4)

print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passengers(self, name):
        self.passengers.append(name)

    def open_seats(self):
        return self.capacity - len(self.passengers)
    

fligt = Flight(3)

fligt.add_passengers('Chika')

print(fligt.passengers)