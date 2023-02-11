class rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = rectangle(a, b)
print("Area of rectangle:", obj.area())

print()