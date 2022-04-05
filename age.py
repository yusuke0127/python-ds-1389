# we are defining the variable age, we are assigning the user input to it
age = int(input("What's your age? "))

# print the age
print(age)

# re-assign the variable age
# age = age + 1
age += 1

# concatenation
# print("Next year, you will be " + str(age) + " years-old!")

# interpolation
print(f"Next year, you will be {age} years-old!")