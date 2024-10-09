import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')

### Column names 
print(df.columns)

### What is the average Length of Stay (LOS)?

# Convert 'length_of_stay' to numeric, forcing errors to NaN
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')

# Calculate the mean, median, std, min, and max for 'length_of_stay'
mean_len_stay = df['length_of_stay'].mean()
print("Mean Length of Stay:", mean_len_stay)

median_len_stay = df['length_of_stay'].median()
print("Median Length of Stay:", median_len_stay)

std_len_stay = df['length_of_stay'].std()
print("Standard Deviation of Length of Stay:", std_len_stay)

min_len_stay = df['length_of_stay'].min()
print("Min Length of Stay:", min_len_stay)

max_len_stay = df['length_of_stay'].max()
print("Max Length of Stay:", max_len_stay)

### Histogram of Length of Stay
plt.figure(figsize=(6, 4))
sns.histplot(df['length_of_stay'], bins=30, kde=True)
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.show()

### How does the Total Cost vary by age group or type of admission?

# Clean the 'total_charges' and 'total_costs' columns
df['total_charges'] = df['total_charges'].str.replace('[\$,]', '', regex=True)
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

df['total_costs'] = df['total_costs'].str.replace('[\$,]', '', regex=True)
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')

# Calculate statistics for 'total_costs'
mean_total_costs = df['total_costs'].mean()
print("Mean Total Costs:", mean_total_costs)

median_total_costs = df['total_costs'].median()
print("Median Total Costs:", median_total_costs)

std_total_costs = df['total_costs'].std()
print("Standard Deviation of Total Costs:", std_total_costs)

min_total_costs = df['total_costs'].min()
print("Min Total Costs:", min_total_costs)

max_total_costs = df['total_costs'].max()
print("Max Total Costs:", max_total_costs)

### Distribution of Age Groups, Gender, and Type of Admission
age_group_count = df['age_group'].value_counts()
print("Age Group Distribution:\n", age_group_count)

gender_count = df['gender'].value_counts()
print("Gender Distribution:\n", gender_count)

type_of_admission_count = df['type_of_admission'].value_counts()
print("Type of Admission Distribution:\n", type_of_admission_count)

### Bar Plot for Age Group Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='age_group', data=df, order=df['age_group'].value_counts().index)
plt.title('Distribution of Age Group')
plt.xlabel('Age Group')
plt.ylabel('Frequency')
plt.show()
