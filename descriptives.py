import pandas as pd
df = pd.read_csv('https://health.data.ny.gov/resource/5dtw-tffi.csv')

### Column names 
df.columns
print(column)

### What is the average Length of Stay (LOS)?

# Display value counts for 'length_of_stay' column
value_counts = df['length_of_stay'].value_counts()
print("Value Counts:\n", value_counts)

# Calculate the mean of the 'length_of_stay' column
mean_value = df['length_of_stay'].describe()
print("Mean:", mean_value)

### histogram Diagram 




### How does the Total Cost vary by age group or type of admission 



## Bar Plot for Type of admissions






### Any noticeable trends in admission or charges? 


### total charges Boxplot 
