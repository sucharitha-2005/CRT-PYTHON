# product of all numbers
nums = input()
t=int(input())
c=0
for i in nums:
    if i.isdigit() and int(i)==t:
        s*=int(i)
print(c)