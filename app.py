from bokeh.io import curdoc
from bokeh.layouts import column,row, layout
from bokeh.models.widgets import TextInput, Button, Paragraph, Select, Slider, Div
from bokeh.plotting import figure, from_networkx
from Scripts.graphvizNetworx import plotAcademicGeneologyTree, generateTree,  plotTree
import networkx as nx


specializations = ['Choose one','all','algorithms-and-complexity', 'artificial-intelligence-and-machine-learning',
'bioinformatics' , 'computer-graphics' ,'cryptography-security-and-privacy-crysp', 'data-systems', 
'formal-methods', 'health-informatics', 'programming-languages', 'scientific-computation',
'software-engineering', 'Quantum computing', 'systems-and-networking']

specialization = ""
generation = 1
plot = plotAcademicGeneologyTree('data-systems', 2)
plot.visible = False

def update_visualization():
    global specialization, generation
    plot.visible = True
    plot.renderers = []
    plot.renderers.append(generateTree(specialization, generation))
    plot.title.text = "Academic Geneology Tree for " + specialization + " with " + str(generation) + " generation(s)"


def update_select(attrname, old, new):
    global specialization, generation
    specialization = new
    update_visualization()

def update_slider(attrname, old, new):
    global specialization, generation
    generation = new
    update_visualization()

header = f"""
    <h1>CS848: The academic geneology of CS professors in UWaterloo</h1>
    <h3>By Jirom Olawuyi</h3>
"""
header = Div(text=header)

# create widgets
specialization_select = Select(
    title = "Select a specialization:",
    value = "Choose one",
    options =  specializations
)

specialization_select.on_change('value', update_select)

generation_slider = Slider(start=1, end=10, value=1, step=1, title="Generation")
generation_slider.on_change('value', update_slider)


# create layout
layouts = layout([header, row(specialization_select, generation_slider), plot], sizing_mode='stretch_both')

# add the layout to curdoc
curdoc().add_root(layouts)