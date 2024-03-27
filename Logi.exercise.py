# Asking the user to input their age
age = int(input("Enter your age: "))

# Asking the user to input whether they are a student or not
student = input("Are you a student? (yes/no): ")

# Using logical operators to deteprmine eligibility for a discount
if age <= 12 or (13 <= age <= 18 and student == 'yes'):
    print("You are eligible for a discount on the movie ticket.")
else:
    print("Sorry, you are not eligible for a discount on the movie ticket.")