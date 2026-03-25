""" 
Mitch Schauer
Sec 02
"""

def getStudent (directory, student):
    return (f"Values Associated with {student}: {directory[student]}")

def getStudentGrades (directory, student):
    if student in directory:
        return directory[student]['grades']
    else:
        return None
    
def getStudentGradeLevel (directory, student):
    if student in directory:
        gradYear = directory[student]['gradYear']
        currentYear = 2026
        gradeLevel = 12 - (gradYear - currentYear)
        return gradeLevel
    else:
        return None
    
def getStudentEmail (directory, student):
    if student in directory:
        return directory[student]['email']
    else:
        return None

def getStudentsByGradeLevel (directory, gradelevel):
    currentYear = 2026
    found = False
    for student, data in directory.items():
        gradYear = data['gradYear']
        gradLevel =  12 - (gradYear - currentYear)
        if gradLevel == gradelevel:
            print(student)
            found = True
    if not found:
        print("Student DNE")

def addStudent (directory):
    check = True
    while check == True:
        name = input("Student Name?\n").strip().lower()
        grades = {}
        recheck = False
        while recheck == False:
            subject = input("Student Name: \n").strip()
            try:
                grade = float(input(f"Grade of {subject}:\n").strip())
                grades[subject] = grade
            except Exception as e:
                print(f"ERROR: {e}")
            reinput = input("Add Another?\n").strip().lower()
            if reinput == 'yes':
                break
            elif reinput == 'no':
                recheck = True
            else:
                print("ERROR")
        while check == True:
            try:
                gradYear = int(input("Student Graduation Year:\n").strip())
                break
            except Exception as e:
                print(f"ERROR: {e}")
        email = input("Student Email?\n").strip()
        directory[name] = {
            'grades': grades,
            'gradYear': gradYear,
            'email': email
        }
        print(f"Student Added: {name}")
        print(directory)
        input1 = input("Add Another?\n").strip().lower()
        if input1 == 'yes':
            print()
        elif input1 == 'no':
            check = False
        else:
            print("ERROR")

def removeStudent (directory, student):
    if student in directory:
        directory.pop(student)
    else:
        print("ERROR")
    print(f"{student} Removed")
    
def updateGrade (directory, student):
    if student not in directory:
        print("ERROR")
        return
    grades = directory[student].get('grades', {})
    check = False
    while check == False:
        print(f"\nCurrent Grades of {student}: {grades}")
        print("1. Add Subject")
        print("2. Remove Subject")
        print("3. Change Existing Grade")
        print("4. Quit")
        input1 = input("Selction:\n")
        if input1 == '1':
            subject = input("Add Subject: ").strip()
            try:
                grade = float(input(f"Grade for {subject}: ").strip())
            except Exception as e:
                print(f"ERROR: {e}")
            grades[subject] = grade
            print(f"Added {subject}: {grade}")
        elif input1 == '2':
            subject = input("Remove Subject: ").strip()
            if subject in grades:
                grades.pop(subject)
                print(f"Removed {subject}")
            else:
                print("ERROR")
        elif input1 == '3':
            subject = input(f"Change Grade?")
            try:
                grade = float(input(f"Grade for {subject}: ").strip())
            except Exception as e:
                print("ERROR: {e}")
            grades(subject) = grade
            print(f"Added {subject}: {grade}")
        elif input1 == '4':
            check = True
        else:
            print("ERROR")
    directory[student]['grades'] = grades
    
def calculateGPA (directory, student):
    if student in directory:
        grades = directory[student]['grades']
        if grades:
            GPA = sum(grades.values()) / len(grades)
            return GPA
        else:
            return 0.0
    else:
        return None
    
def checkHonorRoll (directory, student):
    if student in directory:
        gpa = calculateGPA(directory, student)
        grades = directory[student]['grades']
        if gpa >= 88 and all(grade > 81 for grade in grades.calues()):
            return True
        else:
            return True
    else:
        return False
    
def printMenu():
    print("Welcome to the statistics Calculator!")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Retreive Student")
    print("4. Update Grades")
    print("5. Calculate GPA")
    print("6. Print Students by Grade Level")
    print("7. Quit")
    input1 = input("Enter Selection: ").strip()
    return input1

def main():
    students = {}
    check = False
    while check == False:
        input1 = printMenu()
        if input1 == '1':
            addStudent(students)
            print(students)
        elif input1 == '2':
            reinput = input("Remove Student: \n").lower().strip()
            removeStudent(students, reinput)
        elif input1 == '3':
            rereinput = input("Access Student: \n").lower().strip()
            print(getStudent(students, rereinput))
        elif input1 == '4':
            inputt = input("Update Grade of Student: \n").lower().strip()
            updateGrade(students, inputt)
        elif input1 == '5':
            inputtt = input("Caluculate GPA of Student: \n").lower().strip()
            gpa = calculateGPA(students, inputtt)
            if gpa is not None:
                print(f"GPA of {inputtt}: {gpa}")
            else:
                print("ERROR")
        elif input1 == '6':
            try:
                gl = int(input("Grade Level: \n").strip())
                getStudentsByGradeLevel(students, gl)
            except ValueError:
                print("ERROR")
        elif input1 == '7':
            check = True

if__name__ == "__main__":
    main()