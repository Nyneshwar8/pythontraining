class A:
    def func(self):
     print("HELLO WORLD...!")

class B:

    def func2(self):
       print("HELLO 2nd FUNC")

class C(A,B):

    def func3(self):
      print("HELLO 3rd FUNC")

res=C()
res.func()
res.func2()
res.func3()