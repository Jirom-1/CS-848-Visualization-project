from turtle import color, fillcolor
import pandas as pd
import graphviz
import re


# plot academic genealogy tree

# read data
df = pd.read_csv('datasets/algorithms-and-complexity.csv')

# create graph
dot = graphviz.Digraph("Academic Genealogy", format='png')

def getAdvisorIDs(string):
    numbers = []
    string = string.split(',')
    # print(len(string))
    for s in string:
        numbers.append(int(re.search(r'\d+', s).group()))
    return numbers

def getAdvisorNames(string):
    names = []
    string = string.split(',')
    for s in string:
        names.append(s.split('(')[0].strip())
    return names

def getAdvisorSchools(string):
    schools = []
    string = string.split(',')
    for s in string:
        schools.append(s.split('(')[0].split(')')[0])
    return schools

def getAdvisorYears(string):
    years = []
    string = string.split(',')
    # print(len(string))
    for s in string:
        years.append(int(re.search(r'\d+', s).group()))
    return years

#create UWaterloo professor nodes
for i in range(len(df)):
    dot.node(str(df.loc[i, 'ID']), df.loc[i, 'Name'] + "\n" + str(df.loc[i, 'school']) + "\n" +   str(df.loc[i, 'year']) + "\n" + df.loc[i, 'Specialization'], fillcolor='blue')

# #create advisor nodes
for i in range(len(df)):
    print(i)
    for j in range(len(getAdvisorIDs(df.loc[i, 'advisor_id']))):
        try:
            dot.node(str(getAdvisorIDs(df.loc[i, 'advisor_id'])[j]), getAdvisorNames(df.loc[i, 'advisor_name'])[j] + "\n" + getAdvisorSchools(df.loc[i, 'advisor_school'])[j] + "\n" + str(getAdvisorYears(df.loc[i, 'advisor_year'])[j]))
        except:
            pass

#create edges
for i in range(len(df)):
    for j in range(len(getAdvisorIDs(df.loc[i, 'advisor_id']))):
        try:
            dot.edge(str(getAdvisorIDs(df.loc[i, 'advisor_id'])[j]), str(df.loc[i, 'ID']))
        except:
            pass
print(dot.source)
dot.render('algo-and-complex-tree.gv', view=True)