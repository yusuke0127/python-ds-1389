student = {
  'name': 'Joseph',
  'age': 21,
  'nationality': "USA"
}

print(student)

# useful fonction on dict
print(len(student))
print('name' in student)
print('job' in student)
print('Joseph' in student) # only taking into account the keys
print(student.keys())
print(student.values())
print(student.items())

#CRUD

# Create
student["job"] = "Data Scientist"
print(student)

# Read
print(student["job"])

# Update
student["job"] = "Unemployed"
print(student["job"])

# Delete
del student["job"]
print(student)

print(student.get("job", "Unknown job"))
print(student.get("name", "Unknown name"))

for key, value in student.items():
  print(key + " - " + str(value))