number = int(input())
students = []
grade = []
for i in range(number):
    name = input()
    mark = float(input())
    students.append([name, mark])
    grade.append(mark)

grade = sorted(set(grade))
m = grade[1]
name = []
for val in students:
    if m == val[1]:
        name.append(val[0])

name.sort()
for nm in name:
    print(nm)
