import pandas as pd

data = {
    "employee": ["John", "Sara", "Mike", "Anna", "Tom", "Lisa"],
    "department": ["IT", "HR", "IT", "HR", "IT", "Finance"],
    "salary": [50000, 60000, 55000, 65000, 45000, 70000],
    "age": [25, 31, 29, 35, 22, 40]
}

df = pd.DataFrame(data)

print(df)

# Task 1
# Find all employees whose salary is greater than 50,000.
fil = df[df['salary'] > 50000]

res = fil['employee'].reset_index(drop=True)

print(res)

# Task 2
# Find the average salary for each department.

avg = df.groupby('department')['salary'].mean()
print(avg)

# Task 3
# Find the employee with the highest salary.

s = df[df['salary'] == df['salary'].max()]
print(s)

# highest_paid_employee = df.nlargest(1, 'salary')
# print(highest_paid_employee)



# Task 4
#
# Find the average age of employees whose salary is greater than 50,000.
avg_age = df[df['salary'] > 50000]['age'].mean()
print(avg_age)


# Task 5 — reasoning
# Suppose your manager asks:
# "Which department has the highest average salary?"
# What steps would you take to answer that question?

# i would group by by the department name and then take the average salary of them


# Exercise 2 — Employee Analysis -------------------------------------------------------------------
#
# Use the same df.
#
# Task 1
#
# Find the department with the highest total salary.

cnt = df.groupby('department')['salary'].max()
print(cnt)


# Exercise 3 — Let's combine business thinking with Pandas --------------------------------------------------------------------------------

import pandas as pd

data = {
    "employee": [
        "John", "Sara", "Mike", "Anna", "John",
        "Sara", "Mike", "Anna", "John", "Sara"
    ],
    "department": [
        "IT", "HR", "IT", "HR", "IT",
        "HR", "IT", "HR", "IT", "HR"
    ],
    "month": [
        "Jan", "Jan", "Jan", "Jan", "Feb",
        "Feb", "Feb", "Feb", "Mar", "Mar"
    ],
    "sales": [
        10000, 5000, 12000, 7000, 8000,
        6000, 9000, 8000, 11000, 7000
    ],
    "hours_worked": [
        8, 8, 9, 8, 7, 8, 6, 8, 8, 8
    ]
}

df = pd.DataFrame(data)

print(df)


# Task 1 — Basic aggregation
#
# Calculate the total sales for each department.

ts = df.groupby('department')['sales'].sum()
print(ts)

# Task 2 — Counting
#
# Find the number of records for each employee.

rec = df.groupby(['employee','department']).count()
print(rec)


# Method	What it counts
# .size()	Rows in each group
# .count()	Non-missing values in each column
# .nunique()	Distinct values


# Task 3 — Multiple aggregations
#
# For each department, calculate:
#
# Total sales.
# Average sales per record.
# Total hours worked.

res = df.groupby('department').agg({'sales':['sum'],'sales':['mean'],'hours_worked':['sum']})
print(res)

res = df.groupby('department').agg(
total_sales=('sales', 'sum'),
    max_sales=('sales', 'mean'),
    total_hours=('hours_worked', 'sum')
)
print(res)

# Task 4 — Business metric
#
# Calculate sales per hour for each department.
tot = df.groupby('department')['sales'].sum()
print(tot)
per_hour = tot / df.groupby('department')['hours_worked'].sum()
print(per_hour)

# Series with matching indexes can be aligned by their index labels during arithmetic.
res = df.groupby('department').agg(
    total_sales=('sales', 'sum'),
    total_hours=('hours_worked', 'sum')
)

res['sales_per_hour'] = res['total_sales'] / res['total_hours']

print(res)

# -----------------------------------------------------------------
# Task A — Highest total sales
#
# Find the department with the highest total sales.
#
# Return the department name and its total sales.

sum_dep = df.groupby('department')['sales'].sum().sort_values(ascending=False).head(1)
print(sum_dep)

# Task B — Employee comparison
#
# Calculate total sales and total hours worked for each employee.
#
# Your output should contain one row per employee.

tot_emp = df.groupby('employee').agg( total_Sales = ('sales','sum'), total_hours = ('hours_worked','sum') )
print(tot_emp)



sum_dep = df.groupby('department')['sales'].sum()

highest_department = sum_dep.idxmax()
highest_sales = sum_dep.max()

print(highest_department, highest_sales)

# Here:
#
# .idxmax() returns the index label associated with the maximum value.
# .max() returns the maximum value itself.

# Task C — Best sales per hour
#
# Calculate sales per hour for each employee.
#
# Identify the employee with the highest value.

sales_per_hr = tot_emp['total_Sales'] / tot_emp['total_hours']
print(sales_per_hr)

high_emp = sales_per_hr.sort_values(ascending=False).head(1)
print(high_emp)


# Task D — Conceptual question
#
# Consider these two expressions:
#
# df.groupby('department')['sales'].mean()
#
# and
#
# df.groupby('department').agg(
#     average_sales=('sales', 'mean')
# )

# the difference between both of them is that the common thing that it uses multiple aggregation and another one simply uses the mormal one
# the major difference come in the way it is represented the output , the first one column name should be simply the mean, but the second
# one will show the average sales which shows what the data is about what average it is


# Task E — Handling missing values
#
# Suppose John's sales value for February is missing (NaN).


# it will skip the none and calculate the total value which is not nan



# 3. Next exercise — Data analyst challenge---------------------------------------------------------------------------
#
# Task 1 — Monthly sales by department
#
# Calculate total sales for every department in every month.
#
# Your output should have one row per department and month, or an equivalent grouped structure.

monthly_sales = df.groupby(['month','department']).agg(total_sales = ('sales','sum')).reset_index()
print(monthly_sales)

# Task 2 — Find the best month for each department
#
# Using your result from Task 1, identify the month with the highest total sales for each department.
#
# Don't just find the highest sale in the original DataFrame. The question asks for the month with the highest combined sales.

gp = monthly_sales.groupby(['department']).agg(highest_sales = ('total_sales','max'))
print(gp)

idx = monthly_sales.groupby('department')['total_sales'].idxmax()

print(idx)


best_months = monthly_sales.loc[idx]
print("best_months", best_months)
print(best_months)


# Task 3 — Identify employees whose sales are below average
#
# Calculate each employee's total sales, then identify employees whose total sales are below the average employee total.
#
# Your result should show the employee's name and total sales.


emp_total_Sales = df.groupby('employee').agg(total_sales = ('sales','sum'))
print(emp_total_Sales)

avg_emp_tot = emp_total_Sales['total_sales'].mean()
print(avg_emp_tot)

below_avg = emp_total_Sales[emp_total_Sales['total_sales'] < avg_emp_tot]
print(below_avg)

# ------------------------------------------------------------------------------------------------
df = pd.DataFrame({
    'employee': ['John', 'Mike', 'Sara', 'Anna', 'Tom', 'Lisa'],
    'department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance'],
    'salary': [50000, 70000, 60000, 80000, 45000, 75000]
})

# Your task is to find the highest-paid employee in each department, including their name, department, and salary.\


# p = df.groupby('department').agg( Salary = ('salary','max') ).reset_index()
# Gets the row indices of the highest salary per department and extracts those complete rows
highest_sal_dep  = df.loc[df.groupby('department')['salary'].idxmax()]

print(highest_sal_dep)

# if the case is if more than 1 person is having same salary as highest(in case of tie we use transform('max'))
max_Sal = df.groupby('department')['salary'].transform('max')
print(max_Sal)

highest_sal_dep_tie = df[df['salary']==max_Sal]
print(highest_sal_dep_tie)


# -------------------------------------------------------------------------------------------
# You were asked to find employees whose salary is greater than their department's average salary.

avg_dep_sal = df.groupby('department')['salary'].transform('mean')
print(avg_dep_sal)

avg_emp_dat = df[df['salary'] > avg_dep_sal]

print(avg_emp_dat)

# --------------------------------------
df = pd.DataFrame({
    'employee': ['John', 'Mike', 'Sara', 'Anna', 'Tom', 'Lisa'],
    'department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance'],
    'salary': [50000, 70000, 60000, 80000, 45000, 75000],
    'experience': [2, 5, 3, 7, 1, 6]
})



# Task: Find employees who satisfy BOTH conditions:
#
# Their salary is greater than their department's average salary.
# Their experience is greater than the average experience across the entire company.
#
# Your output should contain the employee name, department, salary, and experience.

avg_experience_company = df['experience'].mean()
print(f" average employee experience of company is {avg_experience_company}")

department_avg_salary = df.groupby('department')['salary'].transform('mean')
print(department_avg_salary)


avg_emps = df[(df['salary'] > department_avg_salary ) & (df['experience'] > avg_experience_company)]

print(f"the average employees are {avg_emps}")

# | Purpose                      | Python condition | Pandas element-wise condition |   |
# | ---------------------------- | ---------------- | ----------------------------- | - |
# | Both conditions must be true | `and`            | `&`                           |   |
# | Either condition can be true | `or`             | `|`                           | ` |
# | Reverse a Boolean condition  | `not`            | `~`                           |   |

# -------------------------------------------------------------
# df = pd.DataFrame({
#     'employee': ['John', 'Mike', 'Sara', 'Anna'],
#     'salary': [30000, 45000, 60000, 80000]
# })

df['salary_category'] = ""

df.loc[df['salary'] < 40000, 'salary_category'] = "Low"
df.loc[(df['salary'] >= 40000 ) & (df['salary'] <= 60000 ), 'salary_category'] = "Medium"
df.loc[df['salary'] > 60000 , 'salary_category'] = "High"

print(df)

df['salary_status'] = ""

df.loc[df['salary'] < 40000 , 'salary_status'] = "Below Average"
df.loc[df['salary'] >= 40000 , 'salary_status'] = "Acceptable"

print(df)


# can be done using apply method
# like using seprate method or single linere function

def salary_status(sal):
    if sal < 40000:
        return "Below Average"
    else:
        return "Acceptable"


df['salary_status'] = df['salary'].apply(salary_status)

# or


df['salary_status'] = df['salary'].apply( lambda  salary : "Below avg" if salary < 40000 else "Acceptable")

print(df)

# Using the same DataFrame, create a function called salary_bonus that follows these rules:
#
# If salary is greater than ₹50,000, return "Bonus Eligible".
# Otherwise, return "Not Eligible".
#
# Your task:
#
# Write the function using def.
# Use .apply() to create a new column named bonus_status.
# Don't use lambda yet.

def sal_bonus(sal):
    if sal > 50000:
        return "Bonus Eligible"
    else:
        return "Not Eligible"

df['salary_bonus'] = df['salary'].apply(sal_bonus)

print(df)


df = pd.DataFrame({
    'employee': ['  JOHN  ', 'sara', '  MiKe', 'ANNA  '],
    'salary': [30000, 45000, 60000, 80000]
})



def clean_names(name):
    return name.lower().strip().capitalize()

df['clean_employee'] = df['employee'].apply(clean_names)
print(df)


df['clean_employee'] = df['employee'].apply(lambda name: name.lower().strip().capitalize())

print(df)

# Great! 😊 Let's finish Day 1 with the four remaining subtasks.-------------------------------------------
df = pd.DataFrame({
    'employee': [' John ', 'SARA', 'mike', 'Anna', 'TOM'],
    'salary': [30000, 45000, None, 80000, 50000],
    'department': ['IT', ' hr ', 'IT', 'HR', ' it ']
})

# Task 1: Create a clean_employee column.
#
# Remove unnecessary spaces.
# Format names consistently, such as John, Sara, and Mike.
#
# Task 2: Create a clean_department column.
#
# Remove unnecessary spaces.
# Convert department names to uppercase.
#
# Task 3: Count the missing values in the salary column.
#
# Task 4: The salary for Mike is missing. Would you replace it with 0, replace it with the average salary, leave it missing while investigating, or delete the row? Explain your reasoning.


def clean_column_vals(val, Capitalise = 1, upper= 0):
    val = val.strip()
    if Capitalise:
        return val.capitalize()
    if upper:
        return val.upper()

df['clean_employee'] = df['employee'].apply(clean_column_vals,args=(1,0))
df['clean_department'] = df['department'].apply(clean_column_vals,args=(0,1))

null_cnt = df['salary'].isna().sum()
print(null_cnt)
print("---------------------------")
print(df)

# -------------------------------------------------------------------------------

df = pd.DataFrame({
    'employee': ['John', 'Sara', 'Mike', 'Anna', 'Tom', 'Lisa'],
    'department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'salary': [50000, 60000, 45000, 80000, None, 55000],
    'experience': [3, 5, 2, 8, 4, 6]
})


# Assessment — 3 questions
#
# Question 1 — Filtering
#
# Find all employees whose salary is greater than ₹50,000.
#
# Return the employee names and salaries.
sal = df[ df['salary'] > 50000 ]
print(sal)

#
# Remember that Mike's and Tom's salaries are different: Mike has ₹45,000, while Tom's salary is missing.
#
# Question 2 — Grouping
#
# Calculate the average salary for each department.
#
# Before writing the code, consider how Pandas handles missing salary values by default when calculating the mean.

# pandas calcultes it as 0 when there is a missing value

avg_sal = df['salary'].mean()
print(avg_sal)

#
# Question 3 — Business reasoning
#
# The manager says:
#
# "The HR department has a higher average salary than IT, so HR employees are performing better."
#
# Do you agree with this conclusion? Explain why or why not.

avg_dep_sal = df.groupby('department')['salary'].mean()
# avg_dep_s = df[df['salary'] >= avg_dep_sal]

print(avg_dep_sal)

# According to the visible data it shows that HR has more avg sal than IT
#but  we cannot fully agree and decide that the HR dept has more avg sal
# than IT because one of the employees salary is missing which is problem here that leads us to think y it happened
# and about the performance the salary itself cant decide , we also need to consider the experience they have that lead to hike in salary
# and also some factors are not shown here like the pressure handlig capacity the amount of work they are getting the levels they are working on and all