class Student:
    def __init__(self):
        self._name=""
    def setname(self,name):
        self._name=name
    def getname(self):
        return self._name


object=Student()
object.setname("Alfaiz")
name=object.getname()
print(name)
