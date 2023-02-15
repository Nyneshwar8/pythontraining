class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

for bird in (obj_bird,obj_spr,obj_ost):
 bird.intro()
 bird.flight()


# obj_bird.intro()
# obj_bird.flight()
#
# obj_spr.intro()
# obj_spr.flight()
#
obj_ost.intro()
obj_ost.flight()


class Dog:
    def __init__(self,str):
        self.name=str

    def hello(self):
            print("bwoo bwoo bwoo")
class cat:
    def __init__(self,str):
        self.name=str

    def hello(self):
            print("Meoow Meoow Meoow")

animals=[Dog("tommy"),cat("Tom")]

for animal in animals:
    animal.hello()

#
# class mom:
#     def __init__(self,str):
#         self.name=str
#
#     def fav(self):
#         print("She is my mother")
# class sis:
#     def __init__(self,str):
#         self.name=str
#
#     def fav(self):
#         print("I love her")
#
# family=[mom("shobha"),sis("Gau")]
#
# for people in family:
#     people.fav()
#


class student:
        def __init__(self):
            self._name=""
        def getname(self):
            return self._name
        def setname(self,name):
            self._name=name
obj=student()
obj.setname("Shubhangi")
_name=obj.getname()
print(_name)