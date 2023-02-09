
List = ['6','6','6','6']
# Uisng all()method
res = all(i == List[0] for i in List)
if (res):
   print("All the elements are SAME")
else:
   print("All Elements are Not SAME")