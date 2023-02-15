class rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

a=10
b=35
obj = rectangle(a, b)
print("Area of rectangle:", obj.area())