

my_str = "We are intern in our company "
words = [letter.lower() for letter in my_str.split()]
words.sort()
print("The sorted words are:")
for letter in words:
   print(letter)