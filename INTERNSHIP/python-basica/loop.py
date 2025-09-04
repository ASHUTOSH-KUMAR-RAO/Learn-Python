# Get all even numbers from 1 to 50, then slice first 20
print("Getting first 20 even numbers from 1 to 50:")

# Step 1: Get all even numbers from 1 to 50
all_even_numbers = [i for i in range(1, 100) if i % 2 == 0]
print(f"All even numbers from 1 to 50: {all_even_numbers}")
print(f"Total even numbers: {len(all_even_numbers)}")  # Will be 25

# Step 2: Slice to get first 20
first_20_evens = all_even_numbers[:20]
print(f"First 20 even numbers: {first_20_evens}")
print(f"Count: {len(first_20_evens)}")



# One line mein 1 to 40 ke squares

squares = [i**2 for i in range(1, 41)] # list initiation 
print(squares)

