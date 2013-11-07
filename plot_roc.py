import numpy as np
import matplotlib.pylab as plt
import sys
fig=plt.figure(frameon=False)
fig.patch.set_visible(False)
ax = fig.add_subplot(111)
ax.grid()

colors=["blue","red","orange","black","green","yellow"]

for idx in range(len(sys.argv[1:])):

    infile = sys.argv[1:][idx]


    data= np.genfromtxt(infile)

    fpr_fisher=data[:,1]
    tpr_fisher=data[:,2]

    fpr_beta = data[:,4]
    tpr_beta = data[:,5]


    ax.set_xlabel("fpr")
    ax.set_ylabel("tpr")
    ax.set_xlim((0,0.5))
    ax.set_ylim((0.5,1))
    #plot lines#
    ax.plot(fpr_fisher,tpr_fisher,
    label='fisher'+infile,
    linestyle="--",
    c=colors[2*idx],
        linewidth=3,
        alpha=1)
    ax.plot(fpr_beta,tpr_beta,c=colors[2*idx+1],
    label='beta'+infile,
    linewidth=3,
    alpha=0.5)
    ######
    """for x,y,thr in zip(fpr_beta,tpr_beta,data[:,3]):
        ax.annotate(thr, xy=(x, y), xytext=(0.1, 0.1), 
        textcoords = 'offset points')"""
    #plot points
    ax.scatter(fpr_fisher,tpr_fisher,marker='o')
    ax.scatter(fpr_beta,tpr_beta,marker='o')
    #
    legend = ax.legend(loc='center right', 
    scatterpoints=1,
    shadow=False,  frameon=False)

fig.suptitle("ROC curves for Z-score,Fisher test, exact beta difference")

plt.show()
