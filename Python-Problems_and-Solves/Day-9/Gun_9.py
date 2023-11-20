if __name__ == '__main__':
    students = []
    for _ in range(int(input(""))):
        name = input("")
        score = float(input(""))
        students.append([name, score])

    # Sort the students based on their grades
    students.sort(key=lambda x: x[1])

    # Find the second lowest grade
    second_lowest_grade = sorted(set([student[1] for student in students]))[1]

    # Get names of students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

    # Sort the names alphabetically
    second_lowest_students.sort()

    # Print names of students with the second lowest grade
    print("\n".join(second_lowest_students))
