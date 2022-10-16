import pandas as pd

specializations = ['algorithms-and-complexity', 'artificial-intelligence-and-machine-learning',
'bioinformatics' , 'computer-graphics' ,'cryptography-security-and-privacy-crysp', 'data-systems', 
'formal-methods', 'health-informatics', 'programming-languages', 'scientific-computation',
'software-engineering', 'Quantum computing', 'systems-and-networking']

# merge all datasets in /datasets folder
def mergeAllDFs():
    df = pd.DataFrame()
    for specialization in specializations:
        df = pd.concat([df, pd.read_csv('datasets/' + specialization + '.csv')], ignore_index=True)
    
    #drop duplicates
    df.drop_duplicates(subset=['Name', 'ID', 'advisor_id'], inplace=True)

    return df

df = mergeAllDFs()
df.to_csv('datasets/all.csv', index=False)
