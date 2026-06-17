import matplotlib.pyplot as mp
import pandas as pd
import numpy as np
    
df = pd.read_csv('StudentData.csv')
print(df,"\n\n")


all_students = ['Ali','Sara','Ahmed','Usman','Ayesha','Bilal']
Names=df["Name"]

student = df[df['Name']=='Ali']
print(student,"\n\n")


subjects = ['Math','Physics','English','Chemistry']

Student_Marks = [student[sub] for sub in subjects]
Student_Name = student['Name']
print(Student_Name)

print(Student_Name+"Marks\n",Student_Marks,"\n\n")

#mp.bar(subjects,Student_Marks)
#mp.title(Student_Name+"'s Marks graph")
#mp.xlabel("subjects")
#mp.ylabel("Marks")

#mp.show()



student_average = df["Average"]

mp.bar(Names, student_average)
mp.title("Average Marks of all students")
mp.show()




