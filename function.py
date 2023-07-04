# build even_or_odd
# define even_or_odd function, with 1 param
# def even_or_odd(num):
#     if num % 2 == 0:
#         return "even"
#     return "odd"

def even_or_odd(num=0):
    return "even" if num % 2 == 0 else "odd"

# call even_or_odd function, passing an argument
print(even_or_odd(12))
print(even_or_odd(42))
print(even_or_odd(13))
print(even_or_odd())