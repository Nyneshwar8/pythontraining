# Program to write student grade
marks=int(input('Enter a Marks:-'))
if marks < 35:
    print('Candidate is FAIL',marks)
elif marks > 35 and marks <=50:
    print('Pass',marks)
elif marks >50 and marks <=60:
    print('second class',marks)
elif marks >60 and marks <=70:
    print('First class',marks)
elif marks >70 and marks <=100:
    print('Distinction')