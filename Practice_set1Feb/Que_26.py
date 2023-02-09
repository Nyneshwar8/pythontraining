# Create three lists of numbers, their squares and cubes.
numbers = []
squares = []
cubes = []

start = 1
end = 10

for count in range (start, end+1) :
    numbers.append (count)
    squares.append (count**2)
    cubes.append (count**3)

print ("numbers: ",numbers)
print ("squares: ",squares)
print ("cubes  : ",cubes)