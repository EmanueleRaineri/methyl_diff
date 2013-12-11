import numpy as np
import matplotlib.pylab as plt
import sys
import pandas as pd
from scipy.stats import gaussian_kde

tp_fisher=pd.read_csv("fisher_of_tp_10_10.txt",header=None)
tn_fisher=pd.read_csv("fisher_of_tn_10_10.txt",header=None)
tp_z=pd.read_csv("zscore_of_tp_10_10.txt",header=None)
tn_z=pd.read_csv("zscore_of_tn_10_10.txt",header=None)
tp_beta=pd.read_csv("beta_of_tp_10_10.txt",header=None)
tn_beta=pd.read_csv("beta_of_tn_10_10.txt",header=None)
#kde = gaussian_kde(tp_fisher)

pvals=[1e-6,1e-5,1e-4,1e-3,5e-2,0.1,0.2,0.5,0.8,1.0]
probs=np.arange(0,1,.1)+0.1
tp_fisher_counts,bins=np.histogram(tp_fisher,bins=pvals)
tn_fisher_counts,bins=np.histogram(tn_fisher,bins=pvals)
tp_z_counts,bins=np.histogram(tp_z,bins=pvals)
tn_z_counts,bins=np.histogram(tn_z,bins=pvals)
tp_beta_counts,beta_bins=np.histogram(tp_beta,bins=probs)
tn_beta_counts,beta_bins=np.histogram(tn_beta,bins=probs)

#[kde(p) for p in pvals]


fig = plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)

ax=fig.add_subplot(231)
center = pvals[:-1] 
ax.set_xlim((1e-6,1e1))
ax.set_ylim((0,1000))
ax.set_xscale('log')
ax.bar(center,tp_fisher_counts,width=center,color='blue')
ax=fig.add_subplot(234)
ax.set_xscale('log')
ax.bar(center,tn_fisher_counts,width=center,color='blue')

ax=fig.add_subplot(232)
ax.set_xscale('log')
ax.set_xlim((1e-6,1e1))
ax.set_ylim((0,1000))
ax.bar(center,tp_z_counts,width=center,color='green')

ax=fig.add_subplot(235)
ax.set_xlim((1e-6,1e1))
ax.set_ylim((0,1000))
ax.set_xscale('log')
ax.bar(center,tn_z_counts,width=center,color='green')

##beta##
print tp_beta_counts
ax=fig.add_subplot(233)
ax.set_xlim((0,1))
ax.set_ylim((0,1000))
#ax.set_xscale('log')
ax.bar(center,tp_beta_counts,width=0.05,color='red')

ax=fig.add_subplot(236)
center = (np.arange(0,1,.1)+0.1)[:-1]
ax.set_xlim((0,1))
ax.set_ylim((0,1000))
#ax.set_xscale('log')
ax.bar(center,tn_beta_counts,width=0.05,color='red')


fig.savefig("fig3.eps", facecolor='w', edgecolor='w', frameon=None)

plt.show()
