student = {
  'name': 'Chris',
  'age': 29,
  'nationality': "Germany"
}

print(student)

# Useful fonction on dict
print(len(student))
print('Chris' in student)
print('age' in student)
print('job' in student)
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

#CRUD

# Create
student['job'] = 'data scientist'
print(student)

# Read (even if the key doesn't exist!)
print(student['age'])
# print(student['hobby']) # KeyError: 'hobby'
print(student.get('age'))
print(student.get('hobby'))
print(student.get('age', 'unknown'))
print(student.get('hobby', 'unknown'))

# Update
student['job'] = 'super data scientist'
print(student)

# Delete
del student['job']
print(student)

# Iterate
for key, value in student.items():
    print(f"{key} - {value}")