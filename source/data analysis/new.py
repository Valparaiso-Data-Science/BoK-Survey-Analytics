import pandas as pd

from bokeh.layouts import row, column
from bokeh.models import Select
from bokeh.palettes import Spectral5
from bokeh.plotting import curdoc, figure
from bokeh.sampledata.autompg import autompg_clean as df
from bokeh.palettes import all_palettes
from bokeh.models.widgets import CheckboxButtonGroup
from bokeh.models.ranges import FactorRange
import numpy as np

dfD = pd.read_pickle("dfdemo.pkl")
dfCourses = pd.read_pickle("courses.pkl")

#TRY HOVERTOOL @CODY
genders = ["She/Her/Hers", "He/Him/His", "Other", np.NaN]
def update(attr):
    print("pee")
    layout.children[1] = create_figure()
def create_figure():

    dfDemo = dfD[dfD["Pronoun"].isin([genders[i] for i in pronoun.active])]

    dfPracts = dfDemo[dfDemo["Primary Role"]=="Data Science Industry Practitioner"]["Position in Firm"].value_counts()
    dfProfs = dfDemo[dfDemo["Primary Role"]=="Data Science Faculty Member/Instructor at Higher Ed Institution"]["Academic position"].value_counts()

    dfBothAcad = dfDemo[dfDemo["Primary Role"]=="Both Practitioner and Faculty Member/Instructor"]["Academic position"].value_counts()
    dfBothFirm = dfDemo[dfDemo["Primary Role"]=="Both Practitioner and Faculty Member/Instructor"]["Position in Firm"].value_counts()
    dfBoth = pd.concat([dfBothAcad,dfBothFirm])
    dfBoth = dfBoth.groupby(dfBoth.index).sum().sort_values(ascending=False)

    dfTotal = pd.DataFrame([dfPracts,dfProfs,dfBothAcad,dfBothFirm],
                          index=["Practitioners","Professors","Both-Academic Position","Both-Industry Position"])

    dfTotal = dfTotal.reindex(['Vice-President', 'Senior','Junior', 'Other (please specify)','Adjunct/Part-Time','Assistant Professor',
          'Associate Professor',  'Full Professor'],
                             axis=1).rename({"Other (please specify)":"Other"},axis=1)

    pt = dfTotal.cumsum(axis=1)
    p = figure(title="Count of Positions of Data Science Professionals",
              x_axis_label='Primary Role', y_axis_label='Total',
              x_range = FactorRange(factors=list(pt.index)),
              plot_height=600, plot_width=900,tools=[])
    for column,color in zip(pt.columns,all_palettes['PiYG'][len(pt.columns)]):
       p.vbar(x=pt.index,bottom=pt[column]-dfTotal[column],top=pt[column],width=.2,color=color, legend = column)
    p.ygrid.minor_grid_line_color = 'black'
    p.ygrid.minor_grid_line_alpha = 0.1



    p.legend.location = "top_left"

    p.toolbar.logo = None
    return p



pronoun = CheckboxButtonGroup(
        labels=["She/Her/Hers", "He/His/Him", "Other","NA"], active=[0,1,2])
pronoun.on_click(update)

controls = column([pronoun], width=200)
layout = row(controls, create_figure())

curdoc().add_root(layout)
