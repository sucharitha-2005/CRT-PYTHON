# program to square the square indexes
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

result = []

for i, num in enumerate(numbers):
    root = int(i ** 0.5)
    if root * root == i:  # index is a perfect square
        result.append(num ** 2)
    else:
        result.append(num)

print(result)