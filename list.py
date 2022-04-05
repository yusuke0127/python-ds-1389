students = ["Deepanjali", "Kevser", "Bryan", "Joe"]
#                0           1         2
print(students)
print(len(students))
print("Chris" in students)
print("Kevser" in students)
print(students[1])
print(students[1:]) # from index 1 to the end
print(students[:1]) # from beginning to index 1 excluded
print(students[1:3]) # from index 1 to index 3 excluded
print(students[-1]) # last element
print(students[-2]) # second last element

# CRUD

# Create
students.append("Gilles")
students.insert(1, "Nayoung")
print(students)

# Read
print(students[1])

# Update
students[1] = "Super Nayoung"
print(students)

# Delete
del students[1]
print(students)

# for student in students:
#     print(student + " is amazing!")

result = [ student + " is amazing!" for student in students ]
print(result)

print(list(enumerate(students)))

for index, student in enumerate(students):
    print(str(index + 1) + " - " + student)