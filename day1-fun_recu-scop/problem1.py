word = "hello"

for ch in word:
    ascii_value = ord(ch)  # Get ASCII value

    if ascii_value % 2 == 0:
        print(f"Character: {ch}, ASCII: {ascii_value}, Even")
    else:
        print(f"Character: {ch}, ASCII: {ascii_value}, Odd")