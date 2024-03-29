from bokeh.plotting import figure, show
from bokeh.sampledata.iris import flowers
from bokeh.transform import factor_cmap, factor_mark

SPECIES = ['setosa', 'versicolor', 'virginica']
MARKERS = ['hex', 'circle_x', 'triangle']

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Sepal Width'

p.scatter("petal_length", "sepal_width", source=flowers, legend="species", fill_alpha=0.8, size=12,
          marker=factor_mark('species', MARKERS, SPECIES),
          color=factor_cmap('species', 'Category10_3', SPECIES))

show(p)