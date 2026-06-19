# Program to print numbers from 10 to 1
# using For Loop, While Loop, and Recursion


def print_using_for():
    print("Numbers using FOR loop:")
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("\n")


def print_using_while():
    print("Numbers using WHILE loop:")
    i = 10
    while i >= 1:
        print(i, end=" ")
        i -= 1
    print("\n")


def print_using_recursion(n):
    if n == 0:  # Base case
        return

    print(n, end=" ")
    print_using_recursion(n - 1)  # Recursive call


# Main Program
print("PRINTING NUMBERS FROM 10 TO 1\n")

print_using_for()

print_using_while()     

print("Numbers using RECURSION:")
print_using_recursion(10)
print()



