# this is a practice file for pandas implementation

import pandas as pd

df = pd.DataFrame(
    {
            "Name": ["Ugwuegbulam, Chima", "West, Kanye", "Winfrey, Oprah", "Takahashi, Rie", "Two, Filler", "Three, Filler",
            "One, Filler"],
            "Age": [21, 45, 68, 28, 45, 67, 18],
            "Sex": ["M", "M", "F", "F", "M", "F", "Other"]
    }
)

# spacer, and print default database
print("------------")
print(df)

# spacer, sort database by age, and print out
print("------------")
print("Sorted by age:")
age_sort = df.sort_values('Age') # put , ascending=False to sort in descending order
print(age_sort)

# spacer, sort database by last name, and print out
print("------------")
print("Sorted by last name: ")
lname_sort = df.sort_values('Name')
print(lname_sort)

# uses .head() to print out first 5 values, and last 5 values from database
print("------------")
print(df.head())
print("------------")
print(df.tail())

#
print("------------")
print()
