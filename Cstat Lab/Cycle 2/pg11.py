import pandas as pd


data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen'],
    'Class': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Subject': ['Math', 'Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'Science'],
    'Marks': [85, 78, 92, 88, 90, 75, 80, 85]
}

df = pd.DataFrame(data)
print(df)

pivot_table = pd.pivot_table(df, values = "Marks", index = "Class", columns = "Subject", aggfunc = "mean")
print(pivot_table)

cross_tab = pd.crosstab(df["Class"], df["Subject"])
print(cross_tab)

