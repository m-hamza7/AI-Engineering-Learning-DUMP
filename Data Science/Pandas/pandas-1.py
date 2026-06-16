import pandas as pd
import numpy as np

data = {}
data['Name'] = ['A', 'B', 'C', 'D']
data['Age'] = [10, 20, 30, 40]
print(data,"\n\n")

df = pd.DataFrame(data)
print(df)

df.index.name = 'ID'
print(df)

df.to_csv('data3.csv', index=True)

df2 = pd.read_csv('data3.csv')
print(df2)

print(df)



df.rename(columns={'Name': 'Full Name', 'Age': 'Age in years'}, inplace=True)

print(df)

df.to_csv('data2.csv', index=False)

df3 = pd.read_csv('data2.csv')
print(df3)



#df. drop('Age in years', axis=1, inplace=True)
print(df)

data2= {'Name': ['Ali', 'Sara', 'Ahmed', 'Usman', 'Ayesha','Bilal','Zara','Hassan', 'Fatima', 'Omar'],
        'Math': [78, 92, 65, 88, 95,55,81,73,90,67],
        'Physics': [85, 89, 70, 76, 98,81,79,68,93,72],
        'English': [70, 95, 60, 84, 92,73,85,75,88,65],
        'Chemistry': [88, 90, 72, 80, 94,68,83,70,91,70]}
df4 = pd.DataFrame(data2)
print("\n\n\n",df4,"\n\n\n")



df4.index.name = 'ID'
df4.to_csv('StudentData.csv',index=True)

studentdata =pd.read_csv('StudentData.csv')
#print(studentdata,"\n\n\n")

datatemp = studentdata.head(3)
#print("\n\n\n",datatemp,"\n\n\n")

maths = studentdata['Math']
#print("maths:\n",maths,"\n\n")

avgmaths = np.mean(maths)

#print("avg maths marks: \n", avgmaths,"\n\n")

#total_marks_ali = studentdata.head(1)['Ali'] 

#print("total marks of ali",total_marks_ali)



print(studentdata.describe())


subjects = ['Math', 'Physics', 'English', 'Chemistry']

studentdata["Total"] = studentdata[subjects].sum(axis=1)

print(studentdata)


studentdata["Average"] = studentdata[subjects].mean(axis=1)

print(studentdata)

studentdata["Grade"] = studentdata["Average"].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else ('C' if x >= 70 else 'D')))
print(studentdata)

studentdata["percentage"] = (studentdata['Total']/(len(subjects)*100))*100
print(studentdata)

studentdata.to_csv('StudentData.csv', index=True)


#print(studentdata.columns)

#print(studentdata.columns.values)

#print(studentdata.index)

#print(studentdata.index.values)



df = pd.read_csv('StudentData.csv')


