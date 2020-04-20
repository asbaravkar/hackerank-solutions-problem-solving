def gradingStudents(n,marks):
    for i in range(n):
        if marks[i]%5>=3 and marks[i]+(5-marks[i]%5)>=40:
            marks[i]=marks[i]+(5-marks[i]%5)
        print(marks[i])
            

n=int(input())
marks=[]
for i in range(n):
    m=int(input())
    marks.append(m)
gradingStudents(n,marks)
