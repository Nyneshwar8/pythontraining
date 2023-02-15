def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Kiwi", "Mango", "Apricot", "Orange"]
map_object = map(starts_with_A, fruit)

print(list(map_object))