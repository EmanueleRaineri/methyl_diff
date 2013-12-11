import numpy as np
import matplotlib.pylab as plt
import sys
import pandas as pd
from scipy.stats import gaussian_kde




fig = plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)

ax=fig.add_subplot(111)



fig.savefig("fig4.eps",  facecolor='w', edgecolor='w', frameon=None)

plt.show()
