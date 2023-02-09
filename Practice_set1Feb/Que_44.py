# Python program to extract keywords from the list
import keyword

# initializing list
test_list = ["Gfg is True", "Gfg will yield a return",
             "Its a global win", "try Gfg"]

# printing original list
print("The original list is : " + str(test_list))

# One-liner using list comprehension
res = [ele for sub in test_list for ele in sub.split() if keyword.iskeyword(ele)]

# printing result
print("Extracted Keywords : " + str(res))