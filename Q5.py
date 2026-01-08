def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Validate inputs
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return False

    # Prevent division by zero
    if divisor == 0:
        return False

    return num % divisor == 0

# Scenario 1
print(check_divisibility(10, 2))  # Expected: True

# Scenario 2
print(check_divisibility(7, 3))   # Expected: False
