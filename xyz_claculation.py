import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import numpy
from numpy.random import randn
from scipy import array, newaxis
column_names = ('frameCount','roiID', 'label', 'xmin', 'ymin', 'xmax', 'ymax', 'detection.spatialCoordinates.x', 'detection.spatialCoordinates.y', 'detection.spatialCoordinates.z')
FEATURE_FILE = r'boxData.csv'
df = pd.read_csv(FEATURE_FILE, sep=',', names=column_names, header=None, encoding='latin-1')
df.head()
df.info()

rows, columns = df.shape
cell_count = rows * columns

data_with_index = df.set_index("label", inplace=True)
ppdf = df.loc["pottedplant"]

print(ppdf)

data_with_index = ppdf.set_index("roiID", inplace=True)
zero = ppdf.loc['0']
print(zero)

one = ppdf.loc['1']
print(one)

two = ppdf.loc['2']
print(two)

#data_with_index.head()



