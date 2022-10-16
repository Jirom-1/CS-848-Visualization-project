from turtle import bgcolor, color, fillcolor
import pandas as pd
import graphviz

def getAdvisorIDs(string):
    numbers = []
    string = string.split(';')
    for s in string:
        if s.isdigit():
            numbers.append(int(s))
    return numbers

def plotAcademicGenealogyTree(specialization, n):
    # plot academic genealogy tree

    # read data
    df = pd.read_csv('../datasets/' + specialization + '.csv')

    # drop duplicates in Name, ID and advisor_id
    df = df.drop_duplicates(subset=['Name', 'ID', 'advisor_id'])

    # drop rows with Generation > n
    df = df[df['Generation'] <= n]
    df = df.reset_index(drop=True)

    # create graph
    dot = graphviz.Digraph("Academic Genealogy for "+ specialization, format='png')

    # add attributes
    # dot.attr('node', fixedsize='both')

    #create professor nodes
    for i in range(len(df)):
        if df['Generation'][i] == 0:
            dot.node(str(df.loc[i, 'ID']), df.loc[i, 'Name'] + "\n" + str(df.loc[i, 'school']) + "\n" +   str(df.loc[i, 'year']) + "\n" + df.loc[i, 'Specialization'], color='blue', fillcolor='lightblue2', style='filled')
        else:
            dot.node(str(df.loc[i, 'ID']), df.loc[i, 'Name'] + "\n" + str(df.loc[i, 'school']) + "\n" +   str(df.loc[i, 'year']) + "\n" + df.loc[i, 'Specialization'])

    #create edges
    for i in range(len(df)):
        for j in range(len(getAdvisorIDs(df.loc[i, 'advisor_id']))):
            try:
                if df.loc[i, 'Generation'] == n:
                    continue
                else:
                    dot.edge(str(getAdvisorIDs(df.loc[i, 'advisor_id'])[j]), str(df.loc[i, 'ID']))
            except:
                pass
    
    dot.render('../AcademicTrees/' + specialization + '-' + str(n) + '.gv', view=True)

specializations = ['algorithms-and-complexity', 'artificial-intelligence-and-machine-learning',
'bioinformatics' , 'computer-graphics' ,'cryptography-security-and-privacy-crysp', 'data-systems', 
'formal-methods', 'health-informatics', 'programming-languages', 'scientific-computation',
'software-engineering', 'Quantum computing', 'systems-and-networking']

for specialization in specializations:
    for n in range(1, 11):
        plotAcademicGenealogyTree(specialization, n)

# plotAcademicGenealogyTree('algorithms-and-complexity', 2)







    