import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv("students.csv")
max_marks_in_maths=df["Math"].max()
min_marks_in_maths=df["Math"].min()
avg_marks_in_maths=df["Math"].mean()
#min,max,mean
print(f"The maximum mark in Maths is : {max_marks_in_maths}")
print(f"The minimum mark in Maths is : {min_marks_in_maths}")
print(f"The average mark in Maths is : {avg_marks_in_maths}")
#gonna make a new column with total marks
df["Total"]=df["Math"]+df["Science"]+df["English"]
#gonna find the topper student based on total marks
topper_student=df.loc[df["Total"].idxmax()]
print(f"The topper student is : {topper_student["Name"]} with total marks of {topper_student["Total"]}")
#finding mean for Science, English, 
avg_marks_in_science=df["Science"].mean()
avg_marks_in_english=df["English"].mean()
print(f"The average mark in Science is : {avg_marks_in_science}")
print(f"The average mark in English is : {avg_marks_in_english}")
#sorting students based on total marks
sorted_df=df.sort_values(by="Total",ascending=False)
print("Students sorted based on total marks:")
print(sorted_df)
#getting students who scored more than avg marks in maths
above_avg_math_tidents=df[df["Math"]>avg_marks_in_maths]
print("Students who scored above average marks in Maths:")
print(above_avg_math_tidents)

#visuaizing data as bar chart
x_axis=np.array(["Math","Science","English"])
y_axis=np.array([avg_marks_in_maths ,avg_marks_in_science,avg_marks_in_english])
plt.bar(x_axis,y_axis)
plt.ylim(0,100)
plt.title("AVG MARKS IN EACH SUBJECT")
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS")

#visualizing data as pie chart
x=df["Name"]
y=df["Total"]
plt.figure(figsize=(8, 8))
plt.pie(y,labels=x,autopct='%1.1f%%', startangle=90)
plt.show()

#saving the new data into a new csv
df.to_csv("students_updated.csv", index=False)

