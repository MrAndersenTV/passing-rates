import pandas as pd

df1 = pd.read_csv("Spanish.csv")
sp_students = df1.to_dict(orient='records')

df2 = pd.read_csv("ELD.csv")
eld_students = df2.to_dict(orient='records')


for student in eld_students:
    print(student)