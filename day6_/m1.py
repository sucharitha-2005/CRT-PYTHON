nums=input().split()
L=len(nums)
nums.reverse()
for i in range(L):
    for j in range(i+1,L):
        print(nums[i],nums[j])