import pandas as pd

# Read the data
df = pd.read_csv('cs_professors.csv')

dataframes = list()

df = df.groupby(by='ID')


#group data by name
for x in df.groups:
    dataframes.append(df.get_group(x).reset_index())

print(len(dataframes))
