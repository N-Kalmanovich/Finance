from datascience import *
import csv
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

viz = Table()

viz = (Table.read_table("Monte.csv"))
viz = viz.relabeled('0', 'Attempts')
viz = viz.relabeled('1', 'Returns')
viz = viz.relabeled('2', 'Risk')

#viz = viz.select("Attempts", "Returns", "Risk")
viz.scatter( 'Risk', 'Returns')

