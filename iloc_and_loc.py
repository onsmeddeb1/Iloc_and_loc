import pandas as pd

data = {
    'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
    'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'],
    'Age': [30, 40, 25, 35, 45, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 70000, 55000],
    'Experience': [3, 7, 2, 5, 10, 4]}

employee_df = pd.DataFrame(data)

first_3_rows = employee_df.iloc[:3]
print(first_3_rows)

marketing_rows = employee_df.loc[employee_df['Department'] == 'Marketing']
print(marketing_rows)

age_gender_first_4 = employee_df.iloc[:4, [2, 3]]
print(age_gender_first_4)

male_salary_experience = employee_df.loc[employee_df['Gender'] == 'Male', ['Salary', 'Experience']]
print(male_salary_experience)