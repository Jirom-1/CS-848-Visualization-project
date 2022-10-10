import pandas as pd
from mathGenealogyWebScraper import scrapeAdvisorIDs, scrapeProfessorDetails
# Read the data
df = pd.read_csv('datasets/algorithms-and-complexity.csv')
errors = list()
for i in range(len(df)):
    # try:
        print(i)
        #scrape ID of each professor's advisor
        print("Scraping advisor IDs")
        print(df['ID'][i])
        advisor_ids = scrapeAdvisorIDs(df['ID'][i])
        df.loc[i, 'advisor_id'] = str(advisor_ids)
        print(advisor_ids)

        #scrape details of each professor's advisor
        print("Scraping advisor details")
        advisor_details = scrapeProfessorDetails(advisor_ids)

        df.loc[i, 'advisor_name'] = str(advisor_details[0])
        df.loc[i, 'advisor_school'] = str(advisor_details[1])
        df.loc[i, 'advisor_year'] = str(advisor_details[2])
    # except:
    #     errors.append(i)
        

df.to_csv('datasets/algorithms-and-complexity.csv', index=False)
print(errors)