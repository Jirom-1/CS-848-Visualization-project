from curses.ascii import isdigit
import pandas as pd
from mathGenealogyWebScraper import scrapeAdvisorIDs, scrapeProfessorDetails
# Read the data


def getNthGeneration(df, n, specialization):
    columns = ['Name', 'Specialization', 'ID', 'school', 'year', 'Generation','advisor_id']
    df_nth = pd.DataFrame(columns=columns)

    #get subset of df where generation is n-1
    df = df[df['Generation'] == n-1].reset_index(drop=True)
    for i in range(len(df)):
        #scrape details of professors in the nth generation from nth-1 generation's advisor IDs
        print("Scraping advisor details")
        for id in df.loc[i, 'advisor_id'].split(';'):
            #check if id is an integer
            if id.isdigit():
                print(id)
                advisor_details = scrapeProfessorDetails(id)
                df_nth.loc[len(df_nth)] = [advisor_details[0], specialization, id, advisor_details[1], advisor_details[2], n, '']
                advisor_ids = scrapeAdvisorIDs(id)
                if len(advisor_ids) == 0:
                    df_nth.loc[len(df_nth)-1, 'advisor_id'] = 'None'
                elif len(advisor_ids) > 1:
                    for i in range(len(advisor_ids)):
                        df_nth.loc[len(df_nth)-1, 'advisor_id'] += str(advisor_ids[i]) + ';'
                else:
                    df_nth.loc[len(df_nth)-1, 'advisor_id'] = str(advisor_ids[0])

    return df_nth



def generateGenerationalDataset(df, n, specialization, generate_zero):
    if generate_zero == True:
        for i in range(len(df)):
            print("Generating 0th generation")
            if str(df.loc[i, 'ID']) != 'nan':
                advisor_ids = scrapeAdvisorIDs(str(int(df.loc[i, 'ID'])))
                print(advisor_ids)
                if len(advisor_ids) == 0:
                    df.loc[i, 'advisor_id'] = 'None'
                elif len(advisor_ids) > 1:
                    for j in range(len(advisor_ids)):
                        df.loc[i, 'advisor_id'] = str(df.loc[i, 'advisor_id']) + str(advisor_ids[j]) + ';'
                else:
                    df.loc[i, 'advisor_id'] = str(advisor_ids)
        print(df)

    try:
        for i in range(1,n+1):
            print("Generation", i)
            df_nth = getNthGeneration(df, i, specialization)
            df = pd.concat([df, df_nth], ignore_index=True)
            # df.to_csv('datasets/' + specialization + '.csv', index=False)
            print(df)
        df.to_csv('datasets/' + specialization + '.csv', index=False)
    except:
        print("Error in generation", i)
        df.to_csv('datasets/' + specialization + '.csv', index=False)
        raise
    
        # df.to_csv('datasets/' + specialization + '.csv', index=False)


specialization = 'artificial-intelligence-and-machine-learning'
df = pd.read_csv('datasets/' + specialization + '.csv')  
print(generateGenerationalDataset(df,1,specialization, True))