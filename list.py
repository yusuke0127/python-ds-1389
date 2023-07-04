students = ["Duong", "Giovanni", "Kanae", "Shiori"]
#                0           1       2         3
#               -4          -3      -2        -1

# Useful fonction on list
print(students)
print(len(students))
print("Vuong" in students)
print("Lucas" in students)
print(students[1])
print(students[1:3]) # every elements from index 1 to index 3 excluded
print(students[1:]) # every elements from index 1 to the end
print(students[:2]) # every elements from the start to index 2 excluded
print(students[-2])

# CRUD

# Create
students.append("Lucas")
print(students)

# Read
print(students[3])

# Update
students[3] = "Super Shiori"
print(students)

# Delete
del students[3]
# students.remove("Super Shiori")
print(students)

# Iterate
for student in students:
    print(f"{student} is amazing!")
    
result = [f"{student} is amazing!" for student in students if student.endswith("g")]
print(result)

# Iterate with index
for index, student in enumerate(students):
    print(f"{index + 1} - {student} is amazing!")
    
print(enumerate(students))
print(list(enumerate(students)))