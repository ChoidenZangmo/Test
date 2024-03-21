# Outer loop
for i in range(1, 10):
    # Check if the outer loop has reached the number 7
    if i == 7:
        break

    # Inner loop
    for j in range(1, 10):
        # Skip the number 3 in the inner loop
        if j == 3:
            continue
        print(j)

    print("End of the outer loop iteration", i)
