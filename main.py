import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql(
    """
    SELECT * 
    FROM employees
    """,
    conn
)

# Step 2
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees
    LIMIT 5
    """,
    conn
)

# Step 3
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees
    LIMIT 5
    """,
    conn
)

# Step 4
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees
    """,
    conn
)

# Step 5
df_executive = pd.read_sql(
    """
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
    """,
    conn
)

# Step 6
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees
    """,
    conn
)

# Step 7
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
    """,
    conn
)

# Step 8
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(SUM(priceEach * quantityOrdered), 0) AS total_price
    FROM orderdetails
    """,
    conn
)

# Step 9
df_day_month_year = pd.read_sql(
    """
    SELECT orderDate,
           strftime('%d', orderDate) AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders
    """,
    conn
)

conn.close()