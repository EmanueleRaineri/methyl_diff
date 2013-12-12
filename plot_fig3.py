import numpy as np
import matplotlib.pylab as plt
import sys
import pandas as pd
from scipy.stats import gaussian_kde


def format_log_ax(ax):
    ax.set_xlim((1e-6,1e0))
    ax.set_ylim((0,1000))
    ax.set_xscale('log')
    ax.xaxis.set_minor_locator(plt.NullLocator())
    return ax

###################
tp_fisher=pd.read_csv("fisher_of_tp_10_10.txt",header=None)
tn_fisher=pd.read_csv("fisher_of_tn_10_10.txt",header=None)
tp_z=pd.read_csv("zscore_of_tp_10_10.txt",header=None)
tn_z=pd.read_csv("zscore_of_tn_10_10.txt",header=None)
tp_beta=pd.read_csv("beta_of_tp_10_10.txt",header=None)
tn_beta=pd.read_csv("beta_of_tn_10_10.txt",header=None)

pvals=np.logspace(-6,0,7)
probs=np.arange( -0.1 , 1.0 , .1 ) + 0.1
tp_fisher_counts,bins=np.histogram(tp_fisher,bins=pvals)
tn_fisher_counts,bins=np.histogram(tn_fisher,bins=pvals)
tp_z_counts,bins=np.histogram(tp_z,bins=pvals)
tn_z_counts,bins=np.histogram(tn_z,bins=pvals)
tp_beta_counts,beta_bins=np.histogram(tp_beta,bins=probs)
tn_beta_counts,beta_bins=np.histogram(tn_beta,bins=probs)
##############################################
fig = plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)
left=pvals[:-1]
w=pvals[1:]-pvals[:-1]
#center = ( pvals[:-1] + pvals[1:] ) / 2
#width = (pvals[1:]- center) 
print "tp_fisher",tp_fisher_counts,bins 
print "tp_beta",tp_beta_counts,beta_bins
# tp fisher
ax=fig.add_subplot(231)
ax=format_log_ax(ax)
ax.bar(left,tp_fisher_counts,width=w,color='blue')
# tn fisher
ax=fig.add_subplot(234)
ax=format_log_ax(ax)
ax.bar(left,tn_fisher_counts,width=w,color='blue')
#tp z
ax=fig.add_subplot(232)
ax=format_log_ax(ax)
ax.bar(left,tp_z_counts,width=w,color='green')
#tn z
ax=fig.add_subplot(235)
ax=format_log_ax(ax)
ax.bar(left,tn_z_counts,width=w,color='green')

left = probs[:-1]
w= 0.1
#tp beta
ax=fig.add_subplot(233)
ax.set_xlim((0,1))
ax.set_ylim((0,1000))
ax.bar(left,tp_beta_counts,width=w,color='red')
#tn beta
ax=fig.add_subplot(236)
ax.set_xlim((0,1))
ax.set_ylim((0,1000))
ax.bar(left,tn_beta_counts,width=w,color='red')
#
fig.savefig("fig3.eps", facecolor='w', edgecolor='w', frameon=None)
plt.show()
