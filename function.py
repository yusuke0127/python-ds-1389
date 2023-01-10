def even_or_odd(number=0):
    """Return even or odd depending on number"""
    # if number % 2 == 0:
    #     return "Even"
    # return "Odd"
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(number=3))
print(even_or_odd(number=4))
print(even_or_odd())