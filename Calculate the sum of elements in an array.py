# Calculate sum of elements in an array

def calculate_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total


# Input
array = [10, 20, 30, 40, 50]

# Function call
result = calculate_sum(array)

# Output
print("Sum of elements is:", result)
