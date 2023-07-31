import random

# Set the number of test cases
t = 7

# Define the range of n and elements of the arrays
n_range = (1, 100)
elem_range = (1, 100)

for i in range(t):
    # Generate n, the length of the arrays
    n = random.randint(*n_range)

    # Generate the elements of the two arrays
    a = [random.randint(*elem_range) for _ in range(n)]
    b = [random.randint(*elem_range) for _ in range(n)]

    # Print the test case
    print(n)
    print(" ".join(map(str, a)))
    print(" ".join(map(str, b)))
