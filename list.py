students = ["Samneang", "Sergei", "Saori", "Sébastien"]
#                0           1       2         3

# Useful fonction on dict
print(len(students))
print("Peter" in students)
print("Samneang" in students)
print(students[1])
print(students[:3]) # from the first to index 3 excluded
print(students[1:3]) # from index 1 to index 3 excluded
print(students[2:3]) # from index 2 to index 3 excluded
print(students[-2]) # 2nd from the end

# CRUD

# Create
students.append("Marvin")
students.insert(2, "Jun")
# students += ["Peter"]
print(students)

# Read
print(students[0])

# Update
students[3] = "Super Saori"
print(students)

# Delete
# del students[3] # remove by index
students.remove("Super Saori") # remove by value
print(students)

# Iterate
# for student in students:
#     print(f"{student} is amazing!")

# Iterate (the List comprehension way)
sentences = [ f"{student} is amazing!" for student in students]
print(sentences)

# Iterate with index
print(list(enumerate(students)))
for index, student in enumerate(students):
    print(f"{index + 1} - {student}")