# Day 4 — Pandas Merge, Joins, Concat & Pivot Tables

# merge() — combine DataFrames using a common column.
# Join types — inner, left, right and outer.
# concat() — stack DataFrames.
# pivot_table() — summarize data in a table format.

import pandas as pd

employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105],
    'employee': ['John', 'Sara', 'Mike', 'Anna', 'Tom'],
    'department_id': [1, 2, 1, 3, 2]
})

print(employees)

departments = pd.DataFrame({
    'department_id': [1, 2, 3, 4],
    'department': ['IT', 'HR', 'Finance', 'Marketing']
})

print(departments)


# Exercise 1----------------------------
# Q1. Merge the DataFrames using department_id and store the result in merged_df.
merged_df = pd.merge(
    employees,
    departments,
    on='department_id',
    how='inner'
)
print(merged_df)
# Q2. Display only these columns from the merged DataFrame:
#
# employee
# department
disp = merged_df[['employee','department']]
print(disp)
#
# Q3. Find all employees who belong to the IT department.
#
IT_deps = merged_df[merged_df['department'] == "IT"]
print(IT_deps)

# Q4. How many employees belong to each department?

print(merged_df.groupby('department')['employee'].count())

# ----------------------------------------
left_df = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'employee': ['John', 'Sara', 'Mike', 'Anna']
})

right_df = pd.DataFrame({
    'emp_id': [102, 103, 105, 106],
    'salary': [50000, 60000, 70000, 80000]
})

ine = pd.merge(left_df, right_df, on='emp_id', how='inner')
print(ine)

lft = pd.merge(left_df, right_df, on='emp_id', how='left')
print(lft)

rgt = pd.merge(left_df, right_df, on='emp_id', how='right')
print(rgt)

otr = pd.merge(left_df, right_df, on='emp_id', how='outer')
print(otr)

# --------------------------------------


employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'employee': ['John', 'Sara', 'Mike', 'Anna']
})

salary = pd.DataFrame({
    'employee_id': [101, 102, 105, 106],
    'salary': [50000, 60000, 70000, 80000]
})

#
# Q1. Perform an INNER JOIN using the two differently named columns.

mrg_df = pd.merge(
    employees,
    salary,
    left_on='emp_id',
    right_on='employee_id',
    how='inner'
)
print(mrg_df)

# Q2. Perform a LEFT JOIN.
mrg_df_l = pd.merge(
    employees,
    salary,
    left_on='emp_id',
    right_on='employee_id',
    how='left'
)
print(mrg_df_l)
# Q3. Perform an OUTER JOIN.
mrg_df_o = pd.merge(
    employees,
    salary,
    left_on='emp_id',
    right_on='employee_id',
    how='outer'
)
print(mrg_df_o)
# Q4. Why do we use left_on and right_on instead of on here?
# because both of the table has common colomns but the column names are different


# ------------------------------
employees = pd.DataFrame({
    'emp_id': [101, 102],
    'employee': ['John', 'Sara']
})

salary = pd.DataFrame({
    'emp_id': [101, 101, 102],
    'month': ['Jan', 'Feb', 'Jan'],
    'salary': [50000, 55000, 60000]
})

# Q1. Merge the two DataFrames using emp_id.
mg_df = pd.merge(
    employees,
    salary,
    on = 'emp_id',
    how = 'outer'
)

print(mg_df)

# Q2. How many rows will the merged DataFrame contain?
# it will contain 3 rows as all are matching and i used the outer join


# Q3. Calculate the total salary paid to each employee using groupby().
total_sal = mg_df.groupby('emp_id')['salary'].sum()
print(total_sal)
total_sal = mg_df.groupby(['emp_id', 'employee'])['salary'].sum()

# Q4. What happens if you use employees.drop_duplicates() after merging? Will it remove John's duplicate salary record correctly, or could it cause a problem?

# it wont remove the duplicate record of john becuse the empid and employee is same but the month and salary are different

# ---------------------------------------


employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'employee': ['John', 'Sara', 'Mike', 'Anna']
})

projects = pd.DataFrame({
    'emp_id': [101, 101, 102, 103, 103, 103],
    'project': ['A', 'B', 'A', 'B', 'C', 'D'],
    'hours': [10, 20, 15, 12, 18, 25]
})

# Q1. Merge employees and projects using emp_id.
# '

mg_df = pd.merge(
    employees,
    projects,
    on='emp_id',
    how='left'
)

print(mg_df)
# Q2. Calculate the total hours worked by each employee.

total_hrs = mg_df.groupby(['emp_id','employee']).agg(Total_hrs = ('hours','sum'))
# total_hrs = mg_df.groupby(['emp_id','employee'])['hours'].transform('sum')
print(total_hrs)


# Q3. Find the employee who worked the highest total hours.
hst = total_hrs.nlargest(1, 'Total_hrs')
print(hst)

# Q4. Find employees who haven't been assigned any projects.
no_prj = mg_df[mg_df['project'].isna()]
print(no_prj)
#
# Q5. Why would an INNER JOIN be unsuitable if management wants a report of all employees, including those without projects?

# inner join only shows the matching eid employees , some of them might not have assigned any projects,
# so outer or left join is better because we can consider the available employees and the avilable projects for them

# --------------------------------------------
jan = pd.DataFrame({
    'employee': ['John', 'Sara'],
    'hours': [160, 150]
})

feb = pd.DataFrame({
    'employee': ['Mike', 'Anna'],
    'hours': [170, 155]
})

# Q1. Combine January and February data vertically into one DataFrame.
mg_df = pd.merge(
    jan,
    feb,
    on='employee',
    how='outer'

)
# this one splits the hours into x and y

print(mg_df)

# Q2. What happens if you use:
#
# pd.concat([jan, feb], axis=0)
# versus:
#
# pd.concat([jan, feb], axis=1)

mg = pd.concat([jan, feb], axis=0).reset_index(drop=True)
print(mg)
# this one joins vertically but with same index as table so make it in a continues we use reset index


mg = pd.concat([jan, feb], axis=1)
print(mg)
# this one add the thing in a row like horizontally, not vertically

# How can you reset the index so the final DataFrame has continuous indexes 0, 1, 2, 3?

# using reset index function setting drop = true anotherwise it will show the old index too


# ---------------------------
jan = pd.DataFrame({
    'employee': ['John', 'Sara'],
    'hours': [160, 150]
})

feb = pd.DataFrame({
    'employee': ['Mike', 'Anna'],
    'overtime': [10, 15]
})

result = pd.concat([jan, feb], axis=0, ignore_index=True)
print(result)
# What will the concat() output look like?
# Why will some values become NaN?
# because some of the values are not availble in both at that time  it shows as nan

# What does ignore_index=True do?
# ignore index preformed exaclty like the reset index drop true, in which it will not consider the index of the table


# verify_intigrity = True , will check if row index labels duplicate or not  for axis 0, for axis 1 it will check column duplicate and raise error


# ------------------
df = pd.DataFrame({
    'employee': ['John', 'John', 'Sara', 'Sara', 'Mike', 'Mike'],
    'project': ['A', 'B', 'A', 'B', 'A', 'B'],
    'hours': [20, 30, 25, 35, 40, 15]
})

# pd.pivot_table(
#     df,
#     values='column_to_calculate',
#     index='rows',
#     columns='columns',
#     aggfunc='sum'
# )

pt = pd.pivot_table(
        df,
        values='hours',
        index=['employee'],
        columns=['project'],
        # aggfunc= sum
        aggfunc= ['sum', 'mean', 'max']
    )


print(pt)

gp = df.groupby(['employee', 'project'])['hours'].sum()
print(gp)

# Q1. Create a pivot table with:
#
# Employees as rows.
# Projects as columns.
# Hours as values.
# Sum as the aggregation function.
#


pvt_tb = pd.pivot_table(
    df,
    index = 'employee',
    columns = 'project',
    values = 'hours',
    aggfunc= 'sum'
)
print(pvt_tb)

# Q2. Add row totals, column totals and the grand total.

pvt_tb = pd.pivot_table(
    df,
    index = 'employee',
    columns = 'project',
    values = 'hours',
    aggfunc= 'sum',
    margins = True
)
print(pvt_tb)

# for column sum
pt.loc['Total'] = pt.sum(axis=0)

# for row
pt.loc['Total'] = pt.sum(axis=1)


# Q3. Change the aggregation function to mean. What changes in the output, and why?
pvt_tb = pd.pivot_table(
    df,
    index = 'employee',
    columns = 'project',
    values = 'hours',
    aggfunc= 'mean',
    margins = True
)
print(pvt_tb)
# it will calulate the mean time a person took in that project

# ---------------------------------
# Q1. Create a pivot table showing the average hours per employee for each project.
#
avg_pt = pd.pivot_table(
    df,
    values = 'hours',
    index = 'employee',
    columns = 'project',
    aggfunc= 'mean',
)
print(avg_pt)
# Q2. Replace missing combinations with 0.
#
avg_pt = pd.pivot_table(
    df,
    values = 'hours',
    index = 'employee',
    columns = 'project',
    aggfunc= 'mean',
    fill_value= 0
)
print(avg_pt)

# Q3. Add row and column totals.
avg_pt = pd.pivot_table(
    df,
    values = 'hours',
    index = 'employee',
    columns = 'project',
    aggfunc= 'mean',
    margins=True
)
print(avg_pt)


# Q4. Business understanding:
#
# John has three records for Project A: 10, 15 and 20 hours.
#
# Explain the difference between the results when using:
#
# aggfunc='sum' : here it calculates the total sum of 3 hours that is 45

# aggfunc='mean' : here it calculates the average of it 45/3 which is 15


# ------------------------------------------Day 4 – Exercise 10: Final Assessment---------------------------------

employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104, 105],
    'employee': ['John', 'Sara', 'Mike', 'Anna', 'David'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR']
})

jan = pd.DataFrame({
    'emp_id': [101, 101, 102, 103, 103],
    'project': ['A', 'B', 'A', 'B', 'C'],
    'hours': [20, 15, 30, 25, 10]
})

feb = pd.DataFrame({
    'emp_id': [101, 102, 102, 103, 105],
    'project': ['A', 'B', 'C', 'A', 'B'],
    'hours': [25, 20, 15, 30, 40]
})



# Q1. Concatenation---------------
#
# Combine January and February timesheets into one DataFrame.

# Hint: Both datasets have the same columns. Think about which axis you need.
#

timesheet = pd.concat(
    [jan, feb],axis=0,ignore_index=True
)

print(timesheet)

# Q2. Merge-------------------
#
# Merge the combined timesheets with the employee master.
#
# Requirements:
#
# Retain all employees, including those who haven't submitted timesheets.
# Include employee name and department.
#
# Hint: Which join type should you use?

mrg_df = pd.merge(
    employees,
    timesheet,
    on='emp_id',
    how='left'
)
print('merged_df')
print(mrg_df)
#
# Q3. GroupBy-----------------------
#
# Calculate the total hours worked by each employee.
#
# Your output should contain:
#
# Employee name
# Total hours

gp = mrg_df.groupby(['emp_id','employee']).agg(Total_hrs = ('hours','sum'))
print(gp)

pvt = mrg_df.pivot_table(
    index = ['emp_id','employee'],
    values = 'hours',
    aggfunc= 'sum'
)
print(pvt)

# Q4. Pivot Table-----------------------
#
# Create a pivot table showing:
#
# Employees as rows.
# Projects as columns.
# Total hours as values.
# Use sum for aggregation.
#
pvt_tb = pd.pivot_table(
    mrg_df,
    index = ['emp_id','employee'],
    columns = 'project',
    values = 'hours',
    aggfunc= 'sum'
)

print(pvt_tb)

# Q5. Pivot Table totals---------------------
#
# Add row totals and column totals to your pivot table.
pvt_tb = pd.pivot_table(
    mrg_df,
    index = ['emp_id','employee'],
    columns = 'project',
    values = 'hours',
    aggfunc= 'sum',
    margins = True
)

print(pvt_tb)
# Q6. Business analysis-------------------------
#
# Answer these questions using Pandas:
#
# Which employee worked the highest number of hours?
hgst = mrg_df.groupby(['emp_id','employee']).agg( total_hrs = ('hours','sum'))
print(hgst)
rnk = hgst['total_hrs'].rank(method='dense', ascending=False)
print(rnk)

print(hgst[rnk == 1])


# Which project received the highest total hours?

hight_prj = mrg_df.groupby('project').agg( total_hrs = ('hours','sum'))
print("highest hours")
print(hight_prj)
highest = hight_prj['total_hrs'].max()
print("highest project")
print(highest)
print(hight_prj[hight_prj['total_hrs'] == highest])
# print("highest project ---------" )
# print(hight_prj.loc[highest])
# print("highest project ---------" )



# Which employee has no timesheet records?

no_ts = mrg_df['project'].isna()
print(no_ts)
n = mrg_df.loc[no_ts]
print(n)


# ---------------------------------------------------

'''

# DAY 4 – PANDAS MERGE, CONCAT, GROUPBY & PIVOT TABLES

## 1. MERGE – Combining DataFrames

**Why do we use it?**

To combine information from two DataFrames using a common column/key.

Example: Combining employee details with salary information using `emp_id`.

### Syntax

```python
pd.merge(
    df1,
    df2,
    on='emp_id',
    how='left'
)
```

### Types of Joins

| Join  | Meaning                                        | When to use                                     |
| ----- | ---------------------------------------------- | ----------------------------------------------- |
| inner | Only matching records                          | Need records present in both tables             |
| left  | All records from left + matching right records | Need to retain all records from the main table  |
| right | All records from right + matching left records | Need to retain all records from the right table |
| outer | All records from both tables                   | Need every record, whether matching or not      |

### Different column names?

Use `left_on` and `right_on`.

```python
pd.merge(
    employees,
    salary,
    left_on='emp_id',
    right_on='employee_id',
    how='left'
)
```

**Remember:**

* Same key name → `on`
* Different key names → `left_on` and `right_on`

### One-to-Many Relationships

If one employee has multiple salary records or works on multiple projects, merging can produce multiple rows for that employee.

This is normal.

Don't use `drop_duplicates()` blindly. First understand what makes a record unique.

---

## 2. CONCAT – Combining DataFrames by Stacking

**Why do we use it?**

To combine datasets that have the same or different structures.

Example: Combining January and February timesheets.

### Vertical Concatenation

```python
result = pd.concat(
    [jan, feb],
    axis=0,
    ignore_index=True
)
```

* `axis=0` → Stack rows vertically.
* `ignore_index=True` → Reset the index.

### Horizontal Concatenation

```python
result = pd.concat(
    [jan, feb],
    axis=1
)
```

* `axis=1` → Place DataFrames side by side.
* Rows are aligned by their index.

### Different Columns?

Pandas automatically takes the union of columns and fills unavailable values with NaN.

**Important difference:**

| Merge                                           | Concat                                |
| ----------------------------------------------- | ------------------------------------- |
| Combines using matching keys                    | Combines by stacking rows or columns  |
| Uses `on`, `left_on`, `right_on`                | Uses `axis`                           |
| Useful for joining employee and project details | Useful for combining monthly datasets |

---

## 3. GROUPBY – Grouping and Aggregating Data

**Why do we use it?**

To calculate summaries for different groups.

Example: Total hours worked by each employee.

### Total hours per employee

```python
df.groupby('employee')['hours'].sum()
```

### Multiple grouping columns

```python
df.groupby(
    ['emp_id', 'employee']
).agg(
    Total_hrs=('hours', 'sum')
)
```

### Common Aggregation Functions

| Function | Meaning                  | When to use                   |
| -------- | ------------------------ | ----------------------------- |
| sum()    | Total                    | Total salary, total hours     |
| mean()   | Average                  | Average salary, average hours |
| max()    | Maximum                  | Highest salary, maximum hours |
| min()    | Minimum                  | Lowest salary, minimum hours  |
| count()  | Count non-missing values | Number of available records   |
| size()   | Count all rows           | Total number of records       |

### Important: Choose the correct grouping column

| Business Question                         | GroupBy    |
| ----------------------------------------- | ---------- |
| Who worked the most hours?                | employee   |
| Which project received the most hours?    | project    |
| Which department has the highest salary?  | department |
| How many records does each employee have? | employee   |

Always understand WHAT you're analysing before choosing `groupby()`.

---

## 4. PIVOT_TABLE – Creating Summary Tables

**Why do we use it?**

To summarise data in a spreadsheet-like format, with groups displayed as rows and columns.

Example:

Original data:

| Employee | Project | Hours |
| -------- | ------- | ----: |
| John     | A       |    20 |
| John     | B       |    30 |
| Sara     | A       |    25 |
| Sara     | B       |    35 |

Pivot table:

| Employee |  A |  B |
| -------- | -: | -: |
| John     | 20 | 30 |
| Sara     | 25 | 35 |

### Basic Syntax

```python
pt = pd.pivot_table(
    df,
    values='hours',
    index='employee',
    columns='project',
    aggfunc='sum'
)
```

### Understanding the Parameters

| Parameter | Purpose                                |
| --------- | -------------------------------------- |
| values    | Column to calculate                    |
| index     | Rows in the pivot table                |
| columns   | Values converted into separate columns |
| aggfunc   | Aggregation function                   |

### When to use different configurations?

**A. Total hours per employee**

```python
pd.pivot_table(
    df,
    values='hours',
    index='employee',
    aggfunc='sum'
)
```

**B. Total hours per project**

```python
pd.pivot_table(
    df,
    values='hours',
    index='project',
    aggfunc='sum'
)
```

**C. Employee-wise project hours**

```python
pd.pivot_table(
    df,
    values='hours',
    index='employee',
    columns='project',
    aggfunc='sum'
)
```

**D. Average hours per employee per project**

```python
pd.pivot_table(
    df,
    values='hours',
    index='employee',
    columns='project',
    aggfunc='mean'
)
```

### Common Aggregations

* `sum` → Total hours.
* `mean` → Average hours.
* `count` → Number of non-missing records.
* `max` → Highest value.
* `min` → Lowest value.

### Handling Missing Values

Use `fill_value=0`:

```python
pd.pivot_table(
    df,
    values='hours',
    index='employee',
    columns='project',
    aggfunc='sum',
    fill_value=0
)
```

This replaces missing pivot-table combinations with zero.

Remember: Missing data does not always mean actual zero hours.

### Adding Row and Column Totals

Use:

```python
margins=True
```

Example:

```python
pd.pivot_table(
    df,
    values='hours',
    index='employee',
    columns='project',
    aggfunc='sum',
    margins=True
)
```

This adds:

* Row totals.
* Column totals.
* Grand total.

**Important:** `margins=True` calculates both row and column totals. It doesn't have separate switches for each.

### Calculating Totals Separately

Row totals:

```python
pt['Total'] = pt.sum(axis=1)
```

Column totals:

```python
pt.loc['Total'] = pt.sum(axis=0)
```

Remember:

| Axis   | Direction    | Result        |
| ------ | ------------ | ------------- |
| axis=0 | Vertically   | Column totals |
| axis=1 | Horizontally | Row totals    |

---

## 5. RANKING AND FINDING THE HIGHEST VALUE

You learned two approaches.

### Method 1: Using rank()

```python
gp = df.groupby('employee').agg(
    total_hrs=('hours', 'sum')
)

rnk = gp['total_hrs'].rank(
    method='dense',
    ascending=False
)

print(gp[rnk == 1])
```

Useful when you need ranking, including multiple employees with tied ranks.

### Method 2: Using max()

```python
highest = gp['total_hrs'].max()

print(gp[gp['total_hrs'] == highest])
```

Useful when you only need the highest value and the corresponding records.

Both approaches preserve ties.

---

## 6. QUICK INTERVIEW REVISION

| Interview Question                                     | Think About               |
| ------------------------------------------------------ | ------------------------- |
| Combine two monthly datasets                           | concat()                  |
| Combine employee and salary details                    | merge()                   |
| Retain all employees, including those without projects | Left join                 |
| Calculate total hours per employee                     | groupby() + sum()         |
| Calculate average salary per department                | groupby() + mean()        |
| Show employees against projects                        | pivot_table()             |
| Add row and column totals                              | margins=True              |
| Replace missing pivot combinations with zero           | fill_value=0              |
| Find highest total hours                               | groupby() + sum() + max() |
| Find employees without timesheets                      | isna()                    |

## 7. COMMON MISTAKES TO AVOID

1. Don't confuse `merge()` with `concat()`.
2. Don't use `max()` when the question asks for total hours.
3. Don't group by employee when the question asks for project-wise analysis.
4. Don't remove repeated employee IDs without understanding the record structure.
5. Don't assume missing values always mean zero.
6. Remember that `mean` calculates averages, while `sum` calculates totals.
7. Read the business question carefully before writing code.

---

### DAY 4 COMPLETED!

Topics covered:

* Merge and join types.
* One-to-many relationships.
* Concat and axis.
* GroupBy and aggregation.
* Pivot tables.
* Row and column totals.
* Missing values.
* Ranking and finding maximum values.

**Your key learning:** Don't memorise code blindly. First understand what the business question is asking, then choose the appropriate Pandas operation.

'''