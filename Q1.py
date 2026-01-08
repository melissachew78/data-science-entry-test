def swap_xy(x, y):
    # Check if both x and y are numeric (int or float)
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Swap using arithmetic (no extra variables)
    x = x + y
    y = x - y
    x = x - y

    print("After swap:")  
    print("x =", x)
    print("y =", y)

# Scenario 1: Non-numeric input
result = swap("Apple", 10)
print(result)   # Expected output: -1

# Scenario 2: Both numeric
swap(9, 17)     # Expected to print swapped values
