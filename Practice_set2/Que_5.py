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








# a = 10
# def outer():
#     a = 20
#     def inner():
#         global a
#         print('10 : ',a) # global chi
#         a = 30
#         def one_more_inner():
#            print("30 :",a)  #10
#         one_more_inner()
#         print("30 :",a)
#
#     inner()
#     print('20 : ',a )
# print("aaa :",a)    #10
# outer()
# print("33 : ",a)    #33

