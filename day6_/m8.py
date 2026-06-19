#linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

# Search
result = linear_search(arr, key)

if result != -1:
    print(f"Element found at position {result + 1}")
else:
    print("Element not found")