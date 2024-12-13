class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(p.x)
print(p.y)


class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if self.open_seats() > 0:
            self.passengers.append(name)
            return True
        return False

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["Dick", "Nick", "Big"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

print(f"Passengers: {flight.passengers}")
