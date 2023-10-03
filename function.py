# Positional argument
def is_even(number):
    return number % 2 == 0

result = is_even(42)
print(result)

# Keyword argument
def is_odd(number=0):
    return number % 2 == 1

result = is_odd(number=1)
print(result)


# Mix of positional and keyword argument
def full_name(first_name, last_name, capitalize=False):
    if capitalize:
        return f"{first_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name} {last_name}"
    

print(full_name("john", "lennon"))
print(full_name("ringo", "starr", capitalize=True))