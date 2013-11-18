import numpy as np
import matplotlib.pylab as plt
import sys

fig=plt.figure(frameon=False)
fig.patch.set_visible(False)
ax = fig.add_subplot(111)
ax.grid()

colors=["blue","red","orange","black","green","yellow"]

print "usage, eg: plot_roc.py roc_10_10.txt roc_20_20.txt"
print "in order: fisher, beta, zscore"

for idx in range(len(sys.argv[1:])):

    infile = sys.argv[1:][idx]
    data= np.genfromtxt(infile)
    #
    fpr_fisher=data[:,1]
    tpr_fisher=data[:,2]
    #
    fpr_beta = data[:,4]
    tpr_beta = data[:,5]
    #
    fpr_zscore = data[:,7]
    tpr_zscore = data[:,8]
    #
    ax.set_xlabel("fpr")
    ax.set_ylabel("tpr")
    ax.set_xlim((0,0.5))
    ax.set_ylim((0.5,1))
    #plot lines#
    #Fisher
    ax.plot(fpr_fisher,tpr_fisher,
    label='Fisher\'s:'+infile,
    linestyle="-",
    c='blue',
    #c=colors[2*idx],
        linewidth=3,
        alpha=1)
    #beta
    ax.plot(fpr_beta,tpr_beta,
    c='red',
    #c=colors[2*idx+1],
    label='beta:'+infile,
    linestyle="-",
    linewidth=3,
    alpha=0.5)
    #Z score
    ax.plot(fpr_zscore,tpr_zscore,
    #c=colors[2*idx+1],
    c='green',
    label='Zscore:'+infile,
    linestyle="-",
    linewidth=3,
    alpha=0.5)
    ######
    """
    for x,y,thr in zip(fpr_beta,tpr_beta,data[:,3]):
    ax.annotate(thr, xy=(x, y), xytext=(0.1, 0.1), 
    textcoords = 'offset points')"""
    #plot points
    ax.scatter(fpr_fisher,tpr_fisher,marker='o',c='blue')
    ax.scatter(fpr_beta,tpr_beta,marker='o',c='red')
    ax.scatter(fpr_zscore,tpr_zscore,marker='o',c='green')
    #
    legend = ax.legend(loc='center right', 
    scatterpoints=1,
    shadow=False,  frameon=False)

fig.suptitle("ROC curves for Z-score,Fisher test, exact beta difference")
plt.show()
