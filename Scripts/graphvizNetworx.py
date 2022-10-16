import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from networkx.drawing.nx_pydot import graphviz_layout
from bokeh.io import output_notebook, show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
import pydot
G = nx.DiGraph()

def getAdvisorIDs(string):
    numbers = []
    string = string.split(';')
    for s in string:
        if s.isdigit():
            numbers.append(str(int(s)))
    return numbers

def generateTree(specialization, n):
    G = nx.DiGraph()
    df = pd.read_csv('datasets/' + specialization + '.csv')

    df = df.drop_duplicates(subset=['Name', 'ID', 'advisor_id'])

    # drop rows with Generation > n
    df = df[df['Generation'] <= n]
    df = df.reset_index(drop=True)


    df['ID'] = df['ID'].astype(str)

    # Add nodes
    for i in range(len(df)):
        if df.loc[i, 'Name'] == 'Jimmy Lin':
            G.add_node(df.loc[i,'ID'], name_=df.loc[i,'Name'], school=df.loc[i, 'school'], year=df.loc[i, 'year'], specialization=df.loc[i, 'Specialization'], color='red')
        elif df.loc[i,'Generation'] == 0:
            G.add_node(df.loc[i,'ID'], name_=df.loc[i,'Name'], school=df.loc[i, 'school'], year=df.loc[i, 'year'], specialization=df.loc[i, 'Specialization'], color='yellow')
        else:
            G.add_node(df.loc[i, 'ID'], name_=df.loc[i, 'Name'], school=df.loc[i, 'school'], year=df.loc[i, 'year'], color='skyblue')

    # Add edges
    for i in range(len(df)):
        if df.loc[i, 'Generation'] == n:
                    continue
        else:
            for j in range(len(getAdvisorIDs(df.loc[i, 'advisor_id']))):
                try:
                    G.add_edge(getAdvisorIDs(df.loc[i, 'advisor_id'])[j], df.loc[i, 'ID'])
                except:
                    pass

    pos = graphviz_layout(G, prog="dot")
    network_graph = from_networkx(G, pos, scale=10, center=(0, 0))

    color = 'color'
    #Set node size and color
    network_graph.node_renderer.glyph = Circle(size=15, fill_color=color)

    #Set edge opacity and width
    network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)
    return network_graph

def plotTree(network_graph, specialization, n):
    pos = graphviz_layout(G, prog="dot")

    #Choose a title!
    title = "Academic Geneology Tree for " + specialization + " with " + str(n) + " generation(s)"

    #Establish which categories will appear when hovering over each node
    HOVER_TOOLTIPS = [("Name", "@name_"), ("School", "@school"), ("Year", "@year")]

    plot = figure(tooltips = HOVER_TOOLTIPS,
                  tools="pan,wheel_zoom,save,reset", active_scroll='wheel_zoom',
                sizing_mode='stretch_width', title=title)

    plot.xgrid.visible = False
    plot.ygrid.visible = False
    plot.axis.visible = False
    plot.renderers.append(network_graph)

    # show(plot)
    # print(type(plot))
    return plot

def plotAcademicGeneologyTree(specialization, n):
    G = generateTree(specialization, n)
    plot = plotTree(G, specialization, n)
    return plot

plotAcademicGeneologyTree('data-systems', 10)