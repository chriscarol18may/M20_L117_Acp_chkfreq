def check_frequency(test_dict, value):
    frequency = list(test_dict.values()).count(value)
    return frequency

# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the test dictionary
print("Test Dictionary:", test_dict)

# Ask user to enter the value for which they want to check frequency
value_to_check = int(input("Enter the value to check its frequency: "))

# Check the frequency of the entered value
frequency = check_frequency(test_dict, value_to_check)

# Print the result
print(f"The frequency of value {value_to_check} in the dictionary is: {frequency}")