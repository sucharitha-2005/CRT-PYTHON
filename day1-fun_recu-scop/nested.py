# Identity Operators Example

a = [1, 2, 3]
b = a              # b refers to the same object as a
c = [1, 2, 3]      # c is a different object with the same values

print("a is b :", a is b)
print("a is c :", a is c)
print("a is not c :", a is not c)
