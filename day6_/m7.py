n=int(input())
c=0
for i in range(2,n**0.5+1):
    if n%i==0:
        c+=1
        print("not a prime")
        break
if c==0:
    print("prime")