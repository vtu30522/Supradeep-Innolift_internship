def sort_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers


size = int(input("Enter the size of the list: "))

numbers = []
for i in range(size):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even, odd = sort_numbers(numbers)

print("Original list:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)