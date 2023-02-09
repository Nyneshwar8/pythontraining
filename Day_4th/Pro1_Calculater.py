#Calculator using list.
def getInput():
    f_num=int(input("Write First number here :-"))
    s_sum=int(input("write Second number here :-"))
    return f_num,s_sum
def add():
   x,y = getInput()
   return x+y
def sub():
    x,y = getInput()
    return  x-y
def mul():
    x, y = getInput()
    return x*y

def div():
    x, y = getInput()
    return x//y
print('''
1.Add
2.Sub
3.Mul
4.Div
''')
choice=int(input("Enter your choice:-"))
operations=[add,sub,mul,div]
output=operations[choice-1]()
print(output)



#Calculater using Dictonary

def getInput():
    f_num=int(input("Write First number here :-"))
    s_sum=int(input("write Second number here :-"))
    return f_num,s_sum

def add():
   x,y = getInput()
   return x+y
def sub():
    x,y = getInput()
    return  x-y
def mul():
    x, y = getInput()
    return x*y

def div():
    x, y = getInput()
    return x//y

def errorHandelar():

    return "invalid credential"

print('''
1.Add
2.Sub
3.Mul
4.Div
''')

choice=int(input("Enter your choice:-"))

operations={
    1:add,
    2:sub,
    3:mul,
    4:div
}
output=operations.get(choice,errorHandelar)()
print(output)