num = 56.00
print(num)
print(round(num, 2))

strNum = str(num)
print("strNum:", strNum)

print(type(strNum))

print(strNum)

new = strNum.replace(".0", ".00")
print(new)

print("------------------")

def aggiusta(floatNum):
    print("float:", floatNum)
    strFloat = str(floatNum)
    punto = strFloat.index('.')
    print("punto:", punto)
    print("lenStr", len(strFloat))
    while (len(strFloat)-1) - punto != 2:
        strFloat += "0"
    print("Stringa aggiustata:", strFloat)

aggiusta(56.0)

aggiusta(45.5)


print("-----------------------------------------")

print("Algoritmo della prova:")
def findPercentage(dictStudents, nameStudent):
    scoresS = dictStudents.get(nameStudent)
    return round(sum(scoresS) / len(scoresS), 2)

def aggiusta(floatNum):
    strFloat = str(floatNum)
    punto = strFloat.index('.')
    while (len(strFloat)-1) - punto != 2:
        strFloat += "0"
    print(strFloat)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = [round(score, 2) for score in scores]
    query_name = input()
    percentage = findPercentage(student_marks, query_name)
    aggiusta(percentage)
