def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Check if key already exists
    if key in dct:
        print("Original value:", dct[key])

    dct[key] = value
    return dct


# Scenario 1
result1 = update_dictionary({}, "name", "Alice")
print(result1)

# Scenario 2
result2 = update_dictionary({"age": 25}, "age", 26)
print(result2)
