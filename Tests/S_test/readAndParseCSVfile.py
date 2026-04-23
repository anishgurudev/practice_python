# | Method            | Best For                   | Returns      | Install Needed?      |
# | ----------------- | -------------------------- | ------------ | -------------------- |
# | csv.reader()      | Simple row-by-row read     | List per row | ❌ No                 |
# | csv.DictReader()  | Access by column name      | Dict per row | ❌ No                 |
# | pandas.read_csv() | Data analysis & filtering  | DataFrame    | ✅ pip install pandas |
# | usecols, nrows    | Large files, partial reads | DataFrame    | ✅ pandas             |
import csv
import pandas as pd

with open("employees.csv", "r") as file:
    reader= csv.reader(file)
    for row in reader:
        print(row)


with open("employees.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


# With pandas:
df = pd.read_csv("employees.csv")
# Access a single column
print(df["name"])               # All names as a Series
print(df["salary"].max())       # Highest salary: 80000
print(df["salary"].min())       # Lowest salary:  50000
print(df["salary"].mean())      # Average salary: 65000.0

# Access specific row (index 0)
print(df.iloc[0])               # First row

# Access specific cell
print(df.loc[0, "name"])        # "Rahul"

# Filter rows
qa_df = df[df["dept"] == "QA"]  # Only QA employees
print(qa_df)

# Read only specific columns
df2 = pd.read_csv("employees.csv", usecols=["name", "salary"])
print(df2)

df = pd.read_csv("employees.csv",sep = ';')

print(df)
