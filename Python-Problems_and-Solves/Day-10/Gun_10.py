# Reading the number of students
n = int(input())

# Creating an empty dictionary to store student records
student_records = {}

# Reading the student records and storing them in the dictionary
for _ in range(n):
    record = input().split()
    name = record[0]
    marks = list(map(float, record[1:]))
    student_records[name] = marks

# Reading the name for which average marks need to be calculated
query_name = input()

# Calculating the average marks for the given student name
if query_name in student_records:
    marks = student_records[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")
else:
    print("Student not found")
