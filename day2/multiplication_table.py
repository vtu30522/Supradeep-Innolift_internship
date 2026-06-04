def times_table(n):
    """Prints the multiplication table for number n from 1×n to 10×n."""
    for i in range(1, 11):
        print(f"{i} × {n} = {i * n}")

# Get input from user
number = int(input("Which number's table do you want? "))
times_table(number)

# Ask user for 3 different numbers for demonstration
print("\n--- Demonstrating with 3 different numbers ---")
for j in range(3):
    num = int(input(f"Enter number {j+1} for demonstration: "))
    print()
    times_table(num)
    print()