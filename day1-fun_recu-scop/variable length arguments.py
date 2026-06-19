def total(*args):
 print(type(args)) # <class 'tuple'>
 return sum(args)
print(total(1, 2, 3)) # 6
print(total(10, 20, 30, 40)) # 100
print(total()) # 0