# This script is used to get the details (school and year of pHD) of the professors from the University of Waterloo

from cmath import nan
import pandas as pd
from mathGenealogyWebScraper import  scrapeProfessorDetails

# Read the data 
df = pd.read_csv('datasets/all_cs_professors.csv')
for i in range(len(df)):
    print(i)
    print(df['ID'][i])
    #if professor ID is not N/A
    if not pd.isna(df['ID'][i]):
        print(df.loc[i, 'Name'])
        try:
            professor_details = scrapeProfessorDetails(int(df.loc[i, 'ID']))
            df.loc[i, 'school'] = professor_details[1]
            df.loc[i, 'year'] = professor_details[2]
        except:
            print(df.loc[i, 'Name'] + ' has no details')

df.to_csv('datasets/all_cs_professors.csv', index=False)