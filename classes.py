class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(3, 4)
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


flight = Flight(3)
people = ['Dick', 'Nick', ' Big']
for people in flight:
    success = flight.add_passengers(people)
print(flight.passengers)
if success:
    print('Added {people} to flight successfully')
else:
    print('No available seats for {person}')
