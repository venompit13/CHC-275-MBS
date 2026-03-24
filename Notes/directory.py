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
        input = input("Add Another?\n").strip().lower()
        if input == 'yes':
            print()
        elif input == 'no':
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
        input = input("Selction:\n")
        if input == '1':
            subject = input("Add Subject: ").strip()
            try:
                grade = float(input(f"Grade for {subject}: ").strip())
            except Exception as e:
                print(f"ERROR: {e}")
            grades[subject] = grade
            print(f"Added {subject}: {grade}")
        elif input == '2':
            subject = input("Remove Subject: ").strip()
            if subject in grades:
                grades.pop(subject)
                print(f"Removed {subject}")
            else:
                print("ERROR")
        elif input == '3':
            subject = input(f"Change Grade?")
            try:
                grade = float(input(f"Grade for {subject}: ").strip())
            except Exception as e:
                print("ERROR: {e}")