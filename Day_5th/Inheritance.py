
class A:
    def funcnction(self):
        print("Welcome.....A")
class B:
    def functionB(self):
        print("Welcome ....B")

class C(A,B):
    def functionC(self):
        print("Welcome.....C")
object=C()
object.funcnction()
object.functionB()
object.functionC()
