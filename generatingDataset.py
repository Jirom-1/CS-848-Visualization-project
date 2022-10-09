import pandas as pd
from mathGenealogyWebScraper import scrapeAdvisorIDs, scrapeProfessorDetails
# Read the data
df = pd.read_csv('datasets/cs_professors.csv')
errors = list()
for i in range(len(df)):
    try:
        print(i)
        #scrape ID of each professor's advisor
        advisor_ids = scrapeAdvisorIDs(df['ID'][i])
        df.loc[i, 'advisor_id'] = advisor_ids

        #scrape details of each professor's advisor
        advisor_details = scrapeProfessorDetails(advisor_ids)

        df.loc[i, 'advisor_name'] = advisor_details[0]
        df.loc[i, 'advisor_school'] = advisor_details[1]
        df.loc[i, 'advisor_year'] = advisor_details[2]
    except:
        errors.append(i)
        

df.to_csv('datasets/cs_professors.csv', index=False)
print(errors)