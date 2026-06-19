def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to check if any swapping happens
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

    return arr


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)
bubble_sort(numbers)
print("Sorted list:", numbers)