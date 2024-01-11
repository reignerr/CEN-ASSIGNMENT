import pandas as pd
import random
import string

def generate_random_matric_numbers(n):
    matric_numbers = ['20CJ027' + ''.join(random.choices(string.digits, k=3)) for _ in range(n)]
    return matric_numbers

def calculate_age(year_of_birth, current_year):
    return current_year - year_of_birth

data = {'Name': ['Chijioke', 'Ngozi', 'Obinna', 'Aisha'],
        'MatricNumber': generate_random_matric_numbers(4),
        'Sex': ['Male', 'Female', 'Male', 'Female'],
        'YearOfBirth': [1996, 1999, 1994, 1997]}

df = pd.DataFrame(data)

df['Age'] = df['YearOfBirth'].apply(lambda x: calculate_age(x, 2024))

print("Original DataFrame:")
print(df)

selected_columns = df[['Name', 'Sex', 'MatricNumber']]
print("\nSelected Columns:")
print(selected_columns)

male_students = df[df['Sex'] == 'Male']
print("\nMale Students:")
print(male_students)

average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

sorted_df = df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame by Age:")
print(sorted_df)
`
