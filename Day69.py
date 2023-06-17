class Triangle:
    def __init__(self):
        print("I am a triangle")

class Isosceles(Triangle):
    def __init__(self):
        super().__init__()
        print("I am an isosceles triangle")

class Equilateral(Isosceles):
    def __init__(self):
        super().__init__()
        print("I am an equilateral triangle")

# Create an object of the Equilateral class
equilateral = Equilateral()
