import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance += self.speed * hours

#Bài 1
car = Car("ABC-123", 142)
print("=== Bài 1: Car Information ===")
print(f"Registration Number: {car.registration_number}")
print(f"Maximum Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Travelled Distance: {car.travelled_distance} km")

#Bài 2
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print("Speed:", car.speed)

car.accelerate(-200)
print("After brake:", car.speed)

#Bài 3
car.drive(1.5)
print("Distance:", car.distance)

#Bài 4
cars = []

for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.randint(150, 200)))

done = False

while not done:
    for c in cars:
        c.accelerate(random.randint(-10, 15))
        c.drive(1)

        if c.distance >= 10000:
            done = True

print("\nResult:")
for c in cars:
    print(c.registration_number, c.max_speed, c.speed, int(c.distance))