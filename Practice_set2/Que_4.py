# ------------1------------
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[9])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of List")


#-----------2----------------
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

finally:
    print("This is finally block.")


# -------------3---------------
# num1=45
# num2=5
# try:
#     res=num1/num2
#     print(res)
# except:
#     print("error:number is not divisible by zero")
# finally:
#     print("Result here")


# -------------4---------------
# ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
# person = input('Get age for: ')
#
# try:
#     print(f'{person} is {ages[person]} years old.')
# except KeyError:
#     print(f"{person}'s age is unknown.")


#------------5---------------
# myDict = {1: 1, 2: 4, 3: 9}
# print("The dictionary is:", myDict)
# key = 2
# if key in myDict.keys():
#     print(myDict[key])
# else:
#     print("{} not a key of dictionary".format(key))

# -------------6--------------------
# countries = {'Italy': 'Rome', 'Poland': 'Warsaw', 'UK': 'London'}
#
# try:
#     print(f'The capital is %s' % countries['London'])
# except KeyError:
#     print('The capital is unknown')

# ------------7-------------------
# def Division(a, b):
#     try:
#         c = ((a + b) / (a - b))
#     except ZeroDivisionError:
#         print("a/b result in 0")
#     else:
#         print(c)
#
# Division(15, 3)
# Division(30, 3)


#-------------8--------------

lit="ADKLRBVN"

# del list[0:5]
# print(list)
print(sorted(lit))