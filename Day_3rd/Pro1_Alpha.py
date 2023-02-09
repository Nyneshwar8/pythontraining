
name="0"

if name >= 'A'  and  name <= 'Z' :
    print("This is Alphabate")
elif name >='a' and name <='z' :
    print("This is Alphabate")
elif name >='0' and name <='9' :
    print("This is Number")
else:
    print("This is not alphabate")


# This is second type to check Alphabat.
a=input("Enter Alphabate here :-")
print(a.isalpha())