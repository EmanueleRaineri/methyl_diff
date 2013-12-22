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
    ax.yaxis.grid()
    return ax

###################
tp_fisher=pd.read_csv("data/fisher_of_p_10_10.txt",header=None,sep=" ")[4]
tn_fisher=pd.read_csv("data/fisher_of_n_10_10.txt",header=None,sep=" ")[4]
tp_z=pd.read_csv("data/zscore_of_p_10_10.txt",header=None,sep=" ")[1]
tn_z=pd.read_csv("data/zscore_of_n_10_10.txt",header=None,sep=" ")[1]
tp_beta=pd.read_csv("data/beta_of_p_10_10.txt",header=None,sep=" ")
tn_beta=pd.read_csv("data/beta_of_n_10_10.txt",header=None,sep=" ")

print tp_fisher,tp_z, tp_beta
pvals = np.logspace(-6,0,7)
probs = np.arange( -0.1 , 1.0 , .1 ) + 0.1

print "pvals,probs",pvals,probs

tp_fisher_counts , bins = np.histogram(tp_fisher,bins=pvals)
tn_fisher_counts , bins = np.histogram(tn_fisher,bins=pvals)

tp_z_counts , bins = np.histogram(tp_z,bins=pvals)
tn_z_counts , bins = np.histogram(tn_z,bins=pvals)

tp_beta_counts , beta_bins = np.histogram(tp_beta,bins=probs)
tn_beta_counts , beta_bins = np.histogram(tn_beta,bins=probs)

print "sums"
print [ np.sum(v) for v in tp_fisher_counts,
    tn_fisher_counts,
    tp_z_counts,
    tn_z_counts,
    tp_beta_counts,
    tn_beta_counts]


##############################################

fig = plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)
left=pvals[:-1]
w=pvals[1:]-pvals[:-1]
print "tp_fisher",tp_fisher_counts,bins 
print "tp_beta",tp_beta_counts,beta_bins
print "left,w",left,w
# tp fisher
ax=fig.add_subplot(231)
ax=format_log_ax(ax)
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.bar(left,tp_fisher_counts,width=w,color='blue')
ax.set_title("Fisher's test")
# tn fisher
ax=fig.add_subplot(234)
ax=format_log_ax(ax)
ax.bar(left,tn_fisher_counts,width=w,color='blue')
ax.set_xlabel("p-value")
ax.set_ylabel("count")
#tp z
ax=fig.add_subplot(232)
ax=format_log_ax(ax)
ax.yaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.bar(left,tp_z_counts,width=w,color='green')
ax.set_title("Z score")
#tn z
ax=fig.add_subplot(235)
ax=format_log_ax(ax)
ax.yaxis.set_major_formatter(plt.NullFormatter())
ax.bar(left,tn_z_counts,width=w,color='green')

left = probs[:-1]
w = 0.1
#tp beta
ax=fig.add_subplot(233)
ax.set_xlim((0,1))
ax.set_ylim((0,1000))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.yaxis.set_major_formatter(plt.NullFormatter())
ax.set_title(r"Beta$_\theta$")
ax.yaxis.grid()
ax.bar(left,tp_beta_counts,width=w,color='red')
#tn beta
ax=fig.add_subplot(236)
ax.set_xlim((0,1))
ax.set_ylim((0,1000))
ax.bar(left,tn_beta_counts,width=w,color='red')
ax.yaxis.set_major_formatter(plt.NullFormatter())
ax.yaxis.grid()
ax.set_xlabel(r"$P\,(\theta_1>\theta_2)$",fontsize=14)
#
fig.text(0.95,0.75,r'$\theta_1>\theta_2$',fontsize=15,rotation='vertical')
fig.text(0.95,0.25,r'$\theta_1=\theta_2$',fontsize=15,rotation='vertical')
#fig.suptitle(r"read depth=10, distribution of p-values and Beta$_\theta$",fontsize=14)
fig.savefig("fig3.eps", facecolor='w', edgecolor='w', frameon=None)
plt.show()
