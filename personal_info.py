# personal_info.py
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")
qualification = input("Enter your dept / course: ")
year = input("Enter your year/sem: ")
cgpa = float(input("Enter your CGPA: "))
city = input("Enter your hometown: ")

print("\n----- STUDENT PROFILE -----")
print(f"Name        : {name}")
print(f"Age         : {age}")
print(f"College     : {college}")
print(f"Department  : {qualification}")
print(f"Year        : {year}")
print(f"CGPA        : {cgpa}")
print(f"Hometown    : {city}")

print(f"\nHello, I am {name}, a {year}, {qualification} student at {college}. "
      f"I am {age} years old, from {city}, with a CGPA of {cgpa}.")