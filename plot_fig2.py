import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
import sys

def lines_of_data(ax,x,y,label,colour): 
    lines,=ax.plot(x,y,
    label=label,
    linestyle="-",
    c=colour, 
    linewidth=1, 
    alpha=0.5)
    ax.scatter(x,y,marker='o',c=colour,lw=0)
    return lines

def make_triplet(ax,data):
    l1 = lines_of_data(ax,data[:,1],data[:,2],"Fisher's test",'blue')
    l2 = lines_of_data(ax,data[:,4],data[:,5],"Beta",'red')
    l3 = lines_of_data(ax,data[:,7],data[:,8],"Z",'green')
    return (l1,l2,l3)

###################


data1 = np.genfromtxt("roc_5_5.txt")
data2 = np.genfromtxt("roc_10_10.txt")
data3 = np.genfromtxt("roc_40_40.txt")

fig=plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)

ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

majorLocator = plt.MultipleLocator(0.1)

for e in [ax1,ax2,ax3]:
    #e.grid()
    e.set_xlim((0,0.4))
    e.set_ylim((0.5,1))
    e.xaxis.set_major_locator(majorLocator)
ax1.set_ylabel("TPR")
ax2.set_xlabel("FPR")
ax2.yaxis.set_major_locator(plt.NullLocator())
ax3.set_ylim((0.8,1))

l1,l2,l3 = make_triplet(ax1,data1)
l4,l5,l6 = make_triplet(ax2,data2)
l7,l8,l9 = make_triplet(ax3,data3)

ax1.set_yticks( [0.50,0.60,0.70,0.80,0.90,1.00])
ax1.yaxis.set_tick_params(direction='in', length=2, width=2, right='off', pad=5)
ax1.set_title("read depth=5")
ax2.set_title("read depth=10")
ax3.set_title("read depth=40")
ax3.yaxis.set_tick_params(direction='in', length=2, width=2, right='off', pad=5)
ax3.set_yticks( [0.85,0.90,0.95,1.00])



ax3.legend( [l7,l8,l9],
    ["Fisher's test","Beta","Z"], 
    loc='lower right' )

#fig.legend([l1,l2,l3],["Fisher's test","Beta","Z"],loc='lower center',ncol=3)
fig.savefig("fig2.eps",  facecolor='w', edgecolor='w', frameon=None)
plt.show( )
