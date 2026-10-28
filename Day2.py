import pandas as pd

df = pd.DataFrame({
    'employee': ['John', 'Sara', 'Mike', 'Anna', 'Tom', 'Lisa'],
    'department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'salary': [50000, 60000, None, 80000, 45000, None],
    'experience': [3, 5, 2, 8, 4, 6]
})

print(df)

print(df.isna().sum())

print(df['salary'].isna())

# df["salary_status"] = df['salary'].apply(lambda sal: "Present" if pd.isna(sal) else "Missing")

print(df)

# Task 1 — Identify missing salaries
#
# Create a new column called salary_status.
#
# Rules:
#
# If salary is missing, assign "Missing".
# Otherwise, assign "Available".
df['salary_status'] = "Available"
df.loc[(pd.isna(df['salary'])) , 'salary_status'] = "Missing"
print(df)

# Task 2 — Calculate departmental averages
#
# Calculate the average salary for each department.
#
# Store the result in a variable called avg_salary.

avg_salary = df.groupby('department').agg(
    avg_salary = ("salary","mean"))

print(avg_salary)

# Task 3 — Find employees earning above their department's average
#
# Create a DataFrame called above_avg containing employees whose salary is greater than their department's average salary.
#
# Important: Don't compare every employee against the overall average. Each employee must be compared against their own department's average.
#
# Hint: Remember the Pandas method we practised on Day 1 that returns a result aligned with every original row, even when calculating a group-level statistic.

dep_mean = df.groupby('department')['salary'].transform('mean')
print(dep_mean)

above_avg = df[df['salary'] > dep_mean]
print(above_avg)


#
# A manager wants to identify employees whose salaries are above their department's average and whose experience is greater than the company's average experience.
#
# Use the same DataFrame.
#
# Your task
#
# Create a DataFrame named qualified_employees containing only employees who satisfy both conditions:
#
# Their salary is greater than their department's average salary.
# Their experience is greater than the company's average experience.
#
# Rules:
#
# Do not change the original salary values.
# Do not fill missing values with zero.
# Use transform() for the department salary average.
# Calculate the company-wide average experience separately.

avg_exp = df['experience'].mean()
print(avg_exp)

above_avg_exp = df[(df['salary'] > dep_mean) & (df['experience'] > avg_exp)]
print(above_avg_exp)

# Your task is to create highest_paid containing the complete row for the highest-paid employee in each department.
#
# Requirements:
#
# Do not include employees with missing salaries.
# Return the employee name, department, salary, and experience.
# If multiple employees in a department have the same highest salary, include all of them.

max_sal = df.groupby('department')['salary'].transform('max')
print(max_sal)

max_sal_people =  df[df['salary'] == max_sal]
print("------------")
print(max_sal_people)


# Your task: Find employees who satisfy ALL THREE conditions:
#
# Their salary is greater than ₹45,000.
# Their experience is greater than 4 years.
# Their salary is not missing.
#
# Return only these columns:
# employee, salary, experience.

df_criteria = df[(df['salary'] > 45000) & (df['experience'] > 4)  & (df['salary'].notna())]

print(df_criteria)


df_criteria = df_criteria[['employee', 'salary', 'experience']]
print(df_criteria)

# "Find the average salary of experienced employees in each department. Consider employees experienced if they have more than 4 years of experience."
# Task 1: Filter employees whose experience is greater than 4 years.
#
# Task 2: Calculate their average salary for each department.
#
# Task 3: Explain what happens to employees whose salary is missing when Pandas calculates the average.
#
# Important: Don't calculate the average across all employees. We want a separate average for each department, considering only experienced employees.

