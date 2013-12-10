import numpy as np
import matplotlib.pylab as plt
import sys
import pandas as pd
from scipy.stats import gaussian_kde

tp_fisher=pd.read_csv("fisher_of_tp_10_10.txt",header=None)
tn_fisher=pd.read_csv("fisher_of_tn_10_10.txt",header=None)

#kde = gaussian_kde(tp_fisher)

pvals=[1e-6,1e-5,1e-4,1e-3,5e-2,0.1,0.2,0.5,0.8,1.0]
tp_fisher_counts,bins=np.histogram(tp_fisher,bins=pvals)
tn_fisher_counts,bins=np.histogram(tn_fisher,bins=pvals)
#[kde(p) for p in pvals]


fig = plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)

ax=fig.add_subplot(231)
center = pvals[:-1] 
ax.set_xscale('log')
ax.bar(center,tp_fisher_counts,width=center)

ax=fig.add_subplot(234)
ax.set_xscale('log')
ax.bar(center,tn_fisher_counts,width=center)


fig.savefig("fig3.eps",  facecolor='w', edgecolor='w', frameon=None)

plt.show()
