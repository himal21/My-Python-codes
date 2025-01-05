import pandas as pd

# Sample CSV data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [50000, 60000, 45000, 70000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('employees.csv', index=False)

# Read from CSV
df = pd.read_csv('employees.csv')

# Calculate average salary
average_salary = df['Salary'].mean()
print(f"Average Salary: ${average_salary:.2f}")

# Filter employees older than 25
older_employees = df[df['Age'] > 25]
print("Employees older than 25:")
print(older_employees)
