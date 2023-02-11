a = 10
def outer():
    a = 20
    def inner():
        global a
        print('SecondPrint : ',a) # global chi
        a = 30
        def one_more_inner():
           print("ThiredPrint :",a)  #10
        one_more_inner()
        print("ForthPrint:",a)

    inner()
    print('FiftPrint: ',a )
print("FirstPrint :",a)    #10
outer()
print("Six: ",a)    #33
