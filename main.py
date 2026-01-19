import csv

students = []

with open("student_data.csv" , "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
    
def result(math, english, attendence):
    average = (math + english) / 2

    if average >= 50 and attendence >= 75:
        return "Pass..."
    else:
        return "fail..."
    
print(students[0])
