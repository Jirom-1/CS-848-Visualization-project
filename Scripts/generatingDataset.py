from curses.ascii import isdigit
import pandas as pd
from mathGenealogyWebScraper import scrapeAdvisorIDs, scrapeProfessorDetails

def extractSpecialization(specialization):
    #read all_cs_professors.csv
    df = pd.read_csv('datasets/all_cs_professors.csv')

    df = df[df['Specialization'] == specialization].reset_index(drop=True)

    #drop rows where ID is NaN
    df = df.dropna(subset=['ID']).reset_index(drop=True)
    return df



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


def generateZerothGeneration(df):

    df['ID'] = df['ID'].astype(int)
    df['ID'] = df['ID'].astype(str)
    
    for i in range(len(df)):
        if df.loc[i, 'ID'] == '0': #This is just for Jimmy Lin
            advisor_ids = ['176620']
        else:
            advisor_ids = scrapeAdvisorIDs(df.loc[i, 'ID'])
        print(advisor_ids)
        if len(advisor_ids) == 0:
            df.loc[i, 'advisor_id'] = 'None'
        elif len(advisor_ids) > 1:
            ids = ""
            for j in range(len(advisor_ids)):
                ids += str(advisor_ids[j]) + ';'
            df.loc[i, 'advisor_id'] = ids
        else:
            df.loc[i, 'advisor_id'] = str(advisor_ids[0])
    print(df)
    return df

def generateGenerationalDataset(specialization, n, generate_zero):
    if generate_zero == True:
        df = extractSpecialization(specialization)
        df = generateZerothGeneration(df)
    
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


specializations = ['cryptography-security-and-privacy-crysp', 'data-systems', 
'formal-methods', 'health-informatics', 'programming-languages', 'scientific-computation',
'software-engineering', 'Quantum computing', 'systems-and-networking']

for specialization in specializations:
    print(specialization)
    generateGenerationalDataset(specialization, 10, True)
