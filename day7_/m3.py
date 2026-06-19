# program to multiply even index with 2 and odd index withh 3
numbers = [10, 20, 30, 40, 50, 60]

result = []

for i in range(len(numbers)):
    if i % 2 == 0:  # even index
        result.append(numbers[i] * 2)
    else:  # odd index
        result.append(numbers[i] * 3)

print(result)