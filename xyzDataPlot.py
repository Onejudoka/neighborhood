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


import csv
from itertools import groupby

#FEATURE_FILE=r'plantdepthframe.csv'
FEATURE_FILE=r'depthFrameData.csv'
#FEATURE_FILE=r'depthFrameData2.csv'
df = pd.read_csv(FEATURE_FILE)
df.fillna(0)

xyz = df.to_numpy()
print(df)

##if

m,n = xyz.shape
R,C = np.mgrid[:m,:n]
out = np.column_stack((C.ravel(),R.ravel(),xyz.ravel()))
print(out)

Xs = out[:,0]
Ys = out[:,1]
Zs = out[:,2]
Zs[Zs>6000]= 0


#x, y, z = x.flatten(), y.flatten(), z.flatten()
#usable_points = (-4 < z) & (z < 4)
#x, y, z = x[usable_points], y[usable_points], z[usable_points]
#ax.plot_trisurf(x, y, z, cmap=cm.jet)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


surf = ax.plot_trisurf(Xs, Ys, Zs, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)
ax.set_zlim(0,30000)
#rotate plot
ax.xaxis.set_major_locator(MaxNLocator(5))
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.zaxis.set_major_locator(MaxNLocator(5))
for angle in range(0,360):
    ax.view_init(60,angle)
fig.tight_layout()

plt.show() # or:
# fig.savefig('3D.png')



#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
#plt.show()

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
#fig.colorbar( surf, shrink=0.5, aspect=5)
#plt.show()

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
#ax.view_init(30, 45)
#plt.show()

#fig = plt.figure()
#ax = fig.gca(projection='3d')
#surf=ax.plot_trisurf(df['Y'], df['X'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
#ax.view_init(30, 45)
#plt.show()













#depthframedata = np.loadtxt("depthFrameData.csv", delimiter=",")




#fname = cbook.get_sample_data('depthFrameData.csv', asfileobj=False)
#with cbook.get_sample_data('depthFrameData.csv') as file:
#    depthFrameData = pd.read_csv(depthFrameData.csv)