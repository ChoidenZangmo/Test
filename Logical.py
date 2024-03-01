# Example 1
x = 5
print(x > 3 and x < 10) #True bcoz both conditions are True

# Example 2 
y = 12
print(y > 10 and y % 5 == 0) # False bcoz both the conditions should be true for 'and' func.
                               # % is a remainder

# Example 1
x = 5
print(x < 3 or x > 10) # False bcoz both conditions are false 

# Example 2
y = 12
print(y < 10 or y % 2 == 0) # True coz second condtion is true. (either one condition can be true to be true)


# Example 1
x = 5
print(not(x > 3 and x < 10)) #False bcoz the condition inside NOT is True

# Example 2
y = 12
print(not(y > 10 and y % 5 == 0)) # True bcoz the condition inside the NOT is False using 'and' operator