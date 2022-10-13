from turtle import color, fillcolor
import pandas as pd
import graphviz

def getAdvisorIDs(string):
    numbers = []
    string = string.split(';')
    # print(len(string))
    for s in string:
        if s.isdigit():
            numbers.append(int(s))
    return numbers

# print(dot.source)

def plotAcademicGenealogyTree(specialization, n):
    # plot academic genealogy tree

    # read data
    df = pd.read_csv('datasets/' + specialization + '.csv')

    # drop duplicates in Name, ID and advisor_id
    df = df.drop_duplicates(subset=['Name', 'ID', 'advisor_id'])

    # drop rows with Generation > n
    df = df[df['Generation'] <= n]
    df = df.reset_index(drop=True)

    # create graph
    dot = graphviz.Digraph("Academic Genealogy for "+ specialization, format='png')

    #create professor nodes
    for i in range(len(df)):
        dot.node(str(df.loc[i, 'ID']), df.loc[i, 'Name'] + "\n" + str(df.loc[i, 'school']) + "\n" +   str(df.loc[i, 'year']) + "\n" + df.loc[i, 'Specialization'], fillcolor='blue')



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
    
    dot.render('AcademicTrees/' + specialization + '.gv', view=True)

plotAcademicGenealogyTree('programming-languages', 10)







    