# let's define the class Bike
class Bike:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")

# let's create a couple instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the Bike class.
print(red_bike.color)               # prints: Red
print(red_bike.frame_material)      # prints: Carbon fiber
print(blue_bike.color)              # prints: Blue
print(blue_bike.frame_material)     # prints: Steel

# let's brake!
red_bike.brake()                    # prints: Braking!
