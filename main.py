import csv
import pandas as pd

students = []

with open("C:/Users/Sathsarani Kangara/Desktop/MY FOLDER/projects/python/student_data.csv" , "r") as file:
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

df = pd.read_csv("student_data.csv")

print(df.head())
print(df.describe())
