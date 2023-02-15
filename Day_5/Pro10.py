vowels = 'aeiou'
str = '''Python also accepts function recursion, 
which means a defined function can call itself. Recursion is a common mathematical and 
programming concept.'''
ip_str = str.casefold()
countChar = {}.fromkeys(vowels,0)
for char in str:
   if char in countChar:
       countChar[char] += 1

print(countChar)
