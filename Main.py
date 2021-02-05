from files.GraphGetter import GraphGetter
from graphical.ChoosePaint import ChoosePaint

# Get graph from file
graph = GraphGetter.get_graph_from_file()

# Show options and graph
ChoosePaint.chooser(graph)
