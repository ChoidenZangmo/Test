# Multiplication table

# Prompt the user to enter the number and limit
num = int(input("Enter the number for which you want the multiplication table: "))
limit = int(input("Enter the limit up to which you want the table generated: "))

# Use a loop to generate the multiplication table
for i in range(1, limit+1):
    print(f"{num} * {i} = {num*i}") 
