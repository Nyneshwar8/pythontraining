

class Product:

    def __init__(self,pid,pnm,ppr,pqty,pcat):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = ppr
        self.prodQty = pqty
        self.prodCate = pcat

    def __str__(self):
        return f''' {self.__dict__}'''

    def __repr__(self):
        return str(self)
P1=Product(1,"mobile",20000,3,"samsung")
print(P1)







# class Product:
#     def __init__(self,ProductId,ProductCategory,ProductPrice,ProductQuntity,ProductName):
#         self.Product_Id=ProductId
#         self.Product_Category=ProductCategory
#         self.Product_Price=ProductPrice
#         self.Product_Quanitity=ProductQuntity
#         self.Product_name=ProductName
#
#     # def __str__(self):
#     #     return f"{self}"
#
#     def __repr__(self):
#         return str(self.__dict__)
#
# ProductList=Product(1,"Mobile",130000,"1","SamsungS23")
# ProductList1=Product(2,"Laptop",225000,"1","Mackbook")
# print(ProductList)
# print(ProductList1)