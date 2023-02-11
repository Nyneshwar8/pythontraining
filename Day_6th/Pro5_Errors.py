
# try:
#     print("code start")
#     print(1 / 0)
# except:
#     print("an error occurs")
# finally:
#     print("GeeksForGeeks")


try:
    amount = 1999
    if amount < 2999:

        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")

except ValueError as e:
    print(e)

