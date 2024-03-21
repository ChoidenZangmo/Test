# Prompt the user to enter the height of the triangle
height = int(input("Enter the height of the triangle: "))

# Use nested loops to print the pattern
for i in range(1, height + 1):
    for j in range(i):
        print('*', end='')
    print()
