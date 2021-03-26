def secondLowestGradeFunc(listaStud):
    grades = sorted([students[1] for students in listaStud])
    lower = grades[0]
    secondLowestGrade = grades[1]
    if lower == secondLowestGrade:
        for i in range(2, len(grades)):
            if grades[i] > secondLowestGrade:
                secondLowestGrade = grades[i]
                break
    return secondLowestGrade

def printNamesSecondLowest(lista, secondLowestGrade):
    result = [name[0] for name in lista if name[1] == secondLowestGrade]
    return result

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    print(students)
    secondLowestGrade = secondLowestGradeFunc(students)
    namesResult = sorted(printNamesSecondLowest(students, secondLowestGrade))
    for name in namesResult:
        print(name)
