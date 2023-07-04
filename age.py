# define an age variable, and assign (store) the user input to it
age = int(input("How old are you? "))

# Concatenation
print("You are " + str(age) + " years-old")
# Interpolation
print(f"You are {age} years-old")

# we re-assign the variable age
# age = age + 1
age += 1

print(f"You are {age} years-old next year")
