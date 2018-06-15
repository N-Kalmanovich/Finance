from datascience import *
import csv
import numpy as np
%matplotlib inline
import matplotlib.pyplot as plt

viz = Table()

viz = (Table.read_table("Keltner.csv").select("Day", "Stock" , "Running Avg", "Lower" , "Upper"))
viz.plot("Day")