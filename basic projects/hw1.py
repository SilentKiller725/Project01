import pandas as pd
from sklearn.linear_model import LinearRegression

student_data={
     'study_hours':[5,5,7,6],
     'final_grade':[3.5,3.6,3.8,3.7]
}

df=pd.DataFrame(student_data)

x=df[['study_hours']]
y=df['final_grade']

model=LinearRegression()

model.fit(x,y)

new_student=[[8]]
prediction=model.predict(new_student)
print(f"predicted grade for new student:{prediction[0]:2f}")