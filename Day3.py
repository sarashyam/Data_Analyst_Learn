import pandas as pd

df = pd.DataFrame({
    'employee': ['John', 'Sara', 'Mike', 'Anna', 'Tom', 'Lisa', 'David', 'Peter'],
    'department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'salary': [50000, 60000, 70000, 80000, 45000, 60000, 70000, 50000],
    'experience': [3, 5, 7, 8, 4, 6, 9, 2]
})



# Exercise 1 – Your turn! 🧠
#
# Using the dataset above, write code for these three tasks:
#
# Q1. Display employees in descending order of salary.

srt_sal = df.sort_values(by=['salary'], ascending=False)
print(srt_sal)


# Q2. Display employees in ascending order of experience.

srt_exp = df.sort_values(by=['experience'], ascending=True)
print(srt_exp)

# Q3. Sort employees:
#
# First by department alphabetically.
# Then by experience from highest to lowest within each department.

srt_dep_exp = df.sort_values(by=['department','experience'], ascending=[True, False])
print(srt_dep_exp)


# Exercise 2 – Your turn!--------------------------------------------
#
# Using our existing DataFrame:
#
# Q1. Find the top 3 highest-paid employees using nlargest().

large_3 = df.nlargest(3,'salary')
print(large_3)


# Q2. Find the 2 employees with the lowest experience using nsmallest().


small_3 = df.nsmallest(2,'experience')
print(small_3)

# Q3. Find the top 2 highest-paid employees in the IT department.

df_hp = df[df['department'] == "IT"].nlargest(2,'salary')
print(df_hp)


# Exercise 3 – Your turn!------------------------------------------
#
# Using our original DataFrame:
#
# Q1. Create a column called salary_rank using default ranking, with the highest salary ranked 1.

sal_rnk = df['salary'].rank(ascending=False)
print(sal_rnk)

# Q2. Create another column called dense_rank using dense ranking.

den_rank = df['salary'].rank(method='dense', ascending=False)
print(den_rank)


# Q3. What is the difference between rank(method='min') and rank(method='dense') when two employees have the same salary?
#  dense method will return the rank with same number if the comparing values are same , like if rank 1 is 50000 and if rank 2 is for salary 45000 for 2 people  then
# the rank 2 is given for both of them
# in min i guess it assigns the same rank like dense but it skips the next rank. like when salary is 30000 it skips rank 3 and assigns 4


df_dup = pd.DataFrame({
    'employee': ['John', 'Sara', 'Mike', 'John', 'Anna', 'Sara'],
    'department': ['IT', 'HR', 'IT', 'IT', 'HR', 'HR'],
    'salary': [50000, 60000, 70000, 50000, 80000, 60000]
})

# Exercise 4 – Your turn!------------------------------------------------
#
# Using df_dup:
#
# Q1. Identify duplicate rows.

# dupli = df_dup.duplicated(keep=False)
dupli = df_dup.duplicated()

print(dupli)

# Q2. Display only the duplicate rows, not the original first occurrences. Use duplicated().


# Q3. Remove duplicate rows and keep the first occurrence.

drp_dupli = df_dup.drop_duplicates(keep='first')
print(drp_dupli)
# Q4. Remove all duplicated rows, including their first occurrences.
drp_dupli_all = df_dup.drop_duplicates(keep=False)
print(drp_dupli_all)

tst = df_dup[dupli]
print(tst)


df_emp = pd.DataFrame({
    'employee_id': [101, 102, 103, 101, 104, 102],
    'employee': ['John', 'Sara', 'Mike', 'John', 'Anna', 'Sara'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'HR'],
    'salary': [50000, 60000, 70000, 55000, 80000, 60000]
})


# Exercise 5 – Your turn! 🧠--------------------------------------------
# Q1. Identify duplicate records based only on employee_id.
dup_eid = df_emp.duplicated(subset=['employee_id'])
print(dup_eid)

# Q2. Display only duplicate records based on employee_id, including the first occurrence.
disp_dup =df_emp.duplicated(subset=['employee_id'],keep=False)
print(disp_dup)

df_new_dup = df_emp[disp_dup]
print(df_new_dup)


# Q3. Remove duplicate records based on employee_id, keeping the last occurrence.
dup_lst = df_emp.drop_duplicates(subset=['employee_id'],keep="last")
print(dup_lst)

# Q4. Are John and Sara duplicates if we consider only employee_id?
# for john it is diffent also the eid but for sara it is the same

# **Q5. Interview question:
#
# Suppose two employees have the same name but different employee IDs.
#
# Should we consider them duplicate employees? Explain your reasoning.
# if employees are having differnt id that is perfeclty fine
# because multiple person can  have same names so it is kinda normal but if the id were same and others are differnt then there will be a problem

# ----------------------------------------

# Q1. Create a department_rank column where the highest salary in each department gets rank 1.

df['department_rank'] = df.groupby('department')['salary'].rank(method='dense', ascending=False)
print(df)

# Q2. Find the top 2 highest-paid employees in each department.
#
# hp = df.groupby('department')['salary'].nlargest(2)
# print(hp)

top_2 = (
    df.groupby('department', group_keys=False)
      .apply(lambda x: x.nlargest(2, 'salary'))
)

print(top_2)


top_2 = df[df['department_rank'] <= 2]
print(top_2)


# Q3. What is the difference between these two?
# df['salary'].rank(ascending=False) : ranks only basis of salary
# df.groupby('department')['salary'].rank(ascending=False) : groups by department and then rank in salary


# ------------------------------------------------------------
df_records = pd.DataFrame({
    'employee_id': [101, 102, 103, 101, 104, 102, 103, 101],
    'employee': ['John', 'Sara', 'Mike', 'John', 'Anna', 'Sara', 'Mike', 'John'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'HR', 'Management'],
    'salary': [50000, 60000, 70000, 55000, 80000, 65000, 75000, 90000],
    'updated_date': [
        '2026-01-10',
        '2026-02-15',
        '2026-01-20',
        '2026-04-10',
        '2026-03-05',
        '2026-05-15',
        '2026-03-20',
        '2026-06-10'
    ]
})



# Exercise 7 – Your tasks
#
# Q1. Convert updated_date into a proper Pandas datetime column using pd.to_datetime().
df_records['updated_date'] = pd.to_datetime(df_records['updated_date'])
print(df_records)

print(df_records.info())
# Q2. Sort the records by updated_date, from oldest to newest.
#
date_sorted = df_records.sort_values(by=['updated_date'], ascending=True)
print(date_sorted)

# Q3. Keep only the latest record for each employee_id.
gp_Date = (
    df_records.groupby('employee_id').apply(lambda x: x.nsmallest(1, 'updated_date'))
)
print(gp_Date)

dp_dupli = date_sorted.drop_duplicates('employee_id', keep='last')
print(dp_dupli)

# Q4. Display only these columns in the final result:
dp_dupli = dp_dupli[['employee_id', 'employee', 'department', 'salary', 'updated_date']]
# employee_id, employee, department, salary, updated_date.
#
# Q5. Interview question:
#
# Why should we sort the records by date before using:

# drop_duplicates(subset=['employee_id'], keep='last')

# this will allow the latest date to be displayed in the bottom which will take the latest dates as last for the bottom


# "I want the second-latest record for each employee instead of the latest record."------------------------
sorted_df = df_records.sort_values('updated_date')
second_latest = (
    sorted_df.groupby('employee_id').nth(-2)
)
print(second_latest)
print("up---------------")
# Q1. Find the latest record for each employee using groupby() and tail().
tl = date_sorted.groupby('employee_id').tail(1)
print(tl)

# Q2. Find the second-latest record for each employee using groupby() and nth().

sec_larg = date_sorted.groupby('employee_id').nth(-2)
print(sec_larg)


# Q3. What does this return? df_records.groupby('employee_id').tail(2)

# it groups according to the employee first and then take the last 2 rows of the particulat values returned from that

df = pd.DataFrame({
    'employee': ['John', 'Sara', 'Mike', 'Anna', 'Tom', 'Lisa', 'David', 'Peter'],
    'department': ['IT', 'HR', 'IT', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'salary': [50000, 60000, 75000, 80000, 45000, 60000, 75000, 50000],
    'experience': [3, 5, 7, 8, 4, 6, 9, 2]
})

# Q1. Find the top 2 highest-paid employees in each department.
#
top_paid = df.groupby('department').apply(lambda x: x.nlargest(2, 'salary'))
print(top_paid)

sals = df.sort_values(by=['salary'], ascending=True)

tops = sals.groupby('department').tail(2)
print(tops)

# Q2. Find all employees whose salary rank is 2 within their department, including ties.
#
dep_rank  = df.groupby('department')['salary'].rank(method='dense', ascending=False)
print(dep_rank)

rank_2 = dep_rank[dep_rank == 2]
print(rank_2)

# Q3. Sort employees by department (A–Z), then salary (highest to lowest).
df_srt = df.sort_values(by=['department','salary'], ascending=[True,False])
# Q4. Find the employee with the highest experience in each department.
hig_exp = df.groupby('department').apply(lambda x: x.nlargest(1, 'experience'))
print(hig_exp)


"""
# DAY 3 – SORTING, RANKING, DUPLICATES & TOP-N ANALYSIS

## 1. SORT_VALUES() – Sorting Data

**Why do we use it?**

To arrange records in ascending or descending order.

### Sort by salary (ascending)

```python
df.sort_values(by='salary')
```

### Sort by salary (descending)

```python
df.sort_values(by='salary', ascending=False)
```

### Sort using multiple columns

```python
df.sort_values(
    by=['department', 'salary'],
    ascending=[True, False]
)
```

This means:

* First sort department alphabetically.
* Within each department, sort salary from highest to lowest.

### Important parameters

| Parameter             | Purpose              |
| --------------------- | -------------------- |
| `by`                  | Column(s) to sort    |
| `ascending=True`      | Smallest to largest  |
| `ascending=False`     | Largest to smallest  |
| `na_position='first'` | Missing values first |
| `na_position='last'`  | Missing values last  |

---

## 2. NLARGEST() AND NSMALLEST()

**Why do we use them?**

To quickly retrieve the top or bottom N records based on a column.

### Top 3 highest salaries

```python
df.nlargest(3, 'salary')
```

### Bottom 2 salaries

```python
df.nsmallest(2, 'salary')
```

### Top 2 salaries in a department

```python
it_df = df[df['department'] == 'IT']

it_df.nlargest(2, 'salary')
```

**Important:**

`nlargest(2)` returns two rows, not necessarily all employees tied at the second-highest rank.

If you need all employees sharing a particular rank, use `rank()`.

---

## 3. RANK() – Ranking Values

**Why do we use it?**

To assign a rank to each record based on a numeric value.

Example:

| Employee | Salary |
| -------- | -----: |
| John     |  50000 |
| Sara     |  60000 |
| Mike     |  70000 |
| Anna     |  80000 |

### Basic ranking

```python
df['rank'] = df['salary'].rank(
    ascending=False
)
```

Highest salary receives rank 1.

### Understanding ranking methods

Suppose salaries are:

| Employee | Salary |
| -------- | -----: |
| Anna     |  80000 |
| Mike     |  70000 |
| Sara     |  70000 |
| John     |  50000 |

#### A. method='average' (default)

Tied values receive the average of their ranks.

| Employee | Rank |
| -------- | ---: |
| Anna     |    1 |
| Mike     |  2.5 |
| Sara     |  2.5 |
| John     |    4 |

#### B. method='min'

Tied values receive the lowest rank in the tied group.

| Employee | Rank |
| -------- | ---: |
| Anna     |    1 |
| Mike     |    2 |
| Sara     |    2 |
| John     |    4 |

#### C. method='dense'

Tied values receive the same rank, without skipping the next rank.

| Employee | Rank |
| -------- | ---: |
| Anna     |    1 |
| Mike     |    2 |
| Sara     |    2 |
| John     |    3 |

#### D. method='first'

Tied values are ranked according to their order in the original data.

### Quick comparison

| Method  | Ranking        |
| ------- | -------------- |
| average | 1, 2.5, 2.5, 4 |
| min     | 1, 2, 2, 4     |
| dense   | 1, 2, 2, 3     |
| first   | 1, 2, 3, 4     |

### Important parameter

```python
ascending=False
```

Means highest value gets rank 1.

```python
ascending=True
```

Means lowest value gets rank 1.

---

## 4. GROUPBY() + RANK()

**Why do we use it?**

To rank records within individual groups.

Example: Rank employees within their departments based on salary.

```python
df['department_rank'] = (
    df.groupby('department')['salary']
    .rank(method='dense', ascending=False)
)
```

This means:

* Group employees by department.
* Rank salaries separately inside each department.
* Highest salary gets rank 1.

Useful for questions like:

* Find the highest-paid employee in each department.
* Rank employees within each department.
* Find the top 3 employees in every department.

### Get all employees ranked first

```python
top_employees = df[
    df['department_rank'] == 1
]
```

This includes ties.

---

## 5. DUPLICATED() – Identifying Duplicate Records

**Why do we use it?**

To identify repeated records in a dataset.

### Find duplicate rows

```python
df.duplicated()
```

Returns True for duplicate rows after the first occurrence.

### Display duplicate rows

```python
df[df.duplicated()]
```

### Check duplicates using specific columns

```python
df[df.duplicated(subset=['emp_id'])]
```

This checks whether an employee ID has appeared previously.

### Keep all occurrences of duplicates

```python
df[df.duplicated(subset=['emp_id'], keep=False)]
```

This displays every occurrence of a duplicated ID, including the first.

---

## 6. DROP_DUPLICATES() – Removing Duplicates

**Why do we use it?**

To remove duplicate records when they are genuinely redundant.

### Remove duplicate rows

```python
df.drop_duplicates()
```

### Keep the first occurrence

```python
df.drop_duplicates(
    subset=['emp_id'],
    keep='first'
)
```

### Keep the last occurrence

```python
df.drop_duplicates(
    subset=['emp_id'],
    keep='last'
)
```

### Remove every occurrence of duplicated IDs

```python
df.drop_duplicates(
    subset=['emp_id'],
    keep=False
)
```

### Important parameters

| Parameter      | Meaning                             |
| -------------- | ----------------------------------- |
| `subset`       | Columns used to identify duplicates |
| `keep='first'` | Keep first occurrence               |
| `keep='last'`  | Keep last occurrence                |
| `keep=False`   | Remove all duplicated occurrences   |

**Important business understanding:**

Repeated employee IDs do not necessarily mean duplicate records.

Example:

| emp_id | Month | Salary |
| ------ | ----- | -----: |
| 101    | Jan   |  50000 |
| 101    | Feb   |  55000 |

These are two different salary records.

Don't remove them just because the employee ID repeats.

---

## 7. SORT + DROP_DUPLICATES – Finding Latest Records

**Why do we use it?**

When a dataset contains multiple records for the same employee and you need only the latest record.

Example:

| Employee ID | Updated Date | Salary |
| ----------- | ------------ | -----: |
| 101         | Jan 10       |  50000 |
| 101         | Mar 15       |  55000 |
| 102         | Feb 20       |  60000 |

First, convert the date column:

```python
df['updated_date'] = pd.to_datetime(
    df['updated_date']
)
```

Sort by date:

```python
df = df.sort_values(
    by='updated_date',
    ascending=True
)
```

Keep the latest record per employee:

```python
latest = df.drop_duplicates(
    subset=['employee_id'],
    keep='last'
)
```

**Remember the sequence:**

1. Convert date to datetime.
2. Sort by date.
3. Remove duplicates while keeping the last record.

---

## 8. GROUPBY() + NLARGEST()

Useful when you want top N values within groups.

Example:

```python
df.groupby('department')['salary'].nlargest(2)
```

This returns the two largest salary values per department.

**Important:** This returns a Series with a MultiIndex, not the complete original rows.

If you want complete employee records, use:

```python
df.sort_values(
    'salary',
    ascending=False
).groupby('department').head(2)
```

This returns the top two rows per department.

Note: `head(2)` returns exactly two rows per group. It does not automatically include every tied employee.

---

## 9. GROUPBY() + TAIL() AND NTH()

These functions help retrieve records from groups based on their current row order.

### Last record per employee

```python
df.groupby('employee').tail(1)
```

### Last two records per employee

```python
df.groupby('employee').tail(2)
```

### Retrieve a particular position

```python
df.groupby('employee').nth(0)
```

First record per group.

```python
df.groupby('employee').nth(-1)
```

Last record per group.

```python
df.groupby('employee').nth(-2)
```

Second-last record per group.

**Important:** These operations use the existing row order. If you need the latest date, sort by date first.

---

# QUICK INTERVIEW REVISION

| Interview Question                 | Concept                             |
| ---------------------------------- | ----------------------------------- |
| Sort employees by salary           | `sort_values()`                     |
| Find top 3 salaries                | `nlargest()`                        |
| Find bottom 2 salaries             | `nsmallest()`                       |
| Rank employees by salary           | `rank()`                            |
| Rank employees within departments  | `groupby() + rank()`                |
| Find all employees with rank 1     | Boolean filtering                   |
| Identify duplicate rows            | `duplicated()`                      |
| Remove duplicate records           | `drop_duplicates()`                 |
| Keep latest employee record        | `sort_values() + drop_duplicates()` |
| Find last two records per employee | `groupby() + tail(2)`               |
| Find top two rows per department   | `sort_values() + groupby().head(2)` |

# COMMON MISTAKES TO AVOID

1. Confusing `nlargest()` with ranking.
2. Forgetting that `rank()` handles ties differently depending on its method.
3. Using `drop_duplicates()` without checking the actual record structure.
4. Forgetting to sort dates before keeping the latest record.
5. Assuming `groupby().tail()` automatically finds the latest record.
6. Confusing `groupby().nlargest()` output with a complete DataFrame.
7. Forgetting that `ascending=False` gives the highest value rank 1.

---

## DAY 3 COMPLETED!

### What you learned

* Sorting records.
* Top-N and bottom-N analysis.
* Ranking and tie handling.
* Department-wise ranking.
* Identifying duplicates.
* Removing duplicates.
* Finding latest records.
* Group-wise top-N analysis.
* Retrieving first, last and nth records.

**Main takeaway:** Before sorting, ranking or removing duplicates, understand the business requirement and the meaning of each record.

"""