import pandas as pd

# # Read the data
data = pd.read_csv('datasets/cs_professors.csv')

#print number of unique names
# print(len(data['Name'].unique()))


# #drop rows where ID is N/A
# data = data.dropna(subset=['ID'])



# drop rows with duplicate names and IDs
# data = data.drop_duplicates(subset=['ID'])
# data = data.drop_duplicates(subset=['Name'])

# print(len(data))
# print(data)


#get list of duplicate names
duplicates = data[data.duplicated(subset=['advisor_name'])]
print(duplicates)

# get list of unique names

# data.to_csv('datasets/cs_professors.csv', index=False)
