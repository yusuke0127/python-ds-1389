student = {
  'name': 'Marvin',
  'age': 29,
  'nationality': "Germany"
}

print(student)

# Useful fonction on dict
print(len(student))
print('Marvin' in student) # "in" doesn't search for values!
print('name' in student) # only keys
print('hi' in student)
print(list(student.values()))
print(list(student.keys()))
print(list(student.items()))

#CRUD

# Create
student['job'] = "Data Scientist"
print(student)

# Read (even if the key doesn't exist!)
print(student['age'])
# print(student['family_name']) # KeyError: 'family_name'
print(student.get('age'))
print(student.get('family_name'))
print(student.get('family_name','not found'))

# Update
student['name'] = 'Super Marvin'
print(student)

# Delete
del student['job']
print(student)

# Iterate
# for key, value in student.items():
#   print(f"{key} - {value}")
  
# [ print(f"{key} - {value}") for key, value in student.items() ]
[ print(f"{key} - {value}") for key, value in student.items() if key.startswith("n")]