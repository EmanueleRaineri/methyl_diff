import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm
import matplotlib as mpl

def histo_2d(ax,x,y,xlabel,ylabel):
    im=ax.hexbin(x,y,bins='log',cmap=cm.Blues)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return im 

def get_inset(fig,coords,y):
    inset = fig.add_axes(coords)
    inset.patch.set_visible(False)
    inset.set_xlim((0.02,1e-6))
    inset.set_yscale('log')
    inset.set_xscale('log')
    inset.set_ylim((0,0.05))
    inset.set_title(r'$1-Beta$',fontsize=10)
    inset.scatter( 1-beta , y , marker='.'  )
    inset.grid()
    majorLocator = plt.FixedLocator([1.5e-2,1e-3,1e-4,1e-5,1e-6])
    majorFormatter=plt.FormatStrFormatter('%.2g')
    inset.xaxis.set_major_locator(majorLocator)
    inset.xaxis.set_minor_locator(plt.NullLocator())
    inset.yaxis.set_minor_locator(plt.NullLocator())
    inset.xaxis.set_major_formatter(majorFormatter)
    for tick in inset.xaxis.get_major_ticks():
        tick.label.set_fontsize(9) 
        tick.label.set_rotation('vertical')
    return inset

#######################################################

#mpl.rc('ps',usedistiller='xpdf')
data = np.genfromtxt( "data/G199.G202.beta.fisher.zscore" , dtype=None )

print data[0]

beta   = np.array([e[11] for e in data])
fisher = np.array([e[12] for e in data])
z      = np.array([e[13] for e in data])

print beta[0],fisher[0],z[0]

fig=plt.figure(figsize=((10,6)),frameon=False)
fig.patch.set_visible(False)

ax1 = fig.add_axes([0.1,0.1,0.35,0.8]) 
ax2 = fig.add_axes([0.50,0.1,0.35,0.8]) 
ax2.yaxis.set_major_locator(plt.NullLocator())
#fig.tight_layout()
im1 = histo_2d( ax1, beta, fisher, "Beta","Fisher's test $p$-value" )
im2 = histo_2d( ax2, beta, z, "Beta","$Z$ score $p$-value" )
#cax = fig.add_subplot(133)
inset1 =  get_inset(fig,[0.15,0.18,0.2,0.2],fisher)
inset2 =  get_inset(fig,[0.55,0.18,0.2,0.2],z)
"""fig.add_axes([0.15,0.18,0.2,0.2])
inset2 = fig.add_axes([0.55,0.15,0.18,0.2])
##############
inset1.set_xlim((0.98,1.0))
inset1.set_yscale('log')
inset1.set_xscale('log')
inset1.set_ylim((0,0.05))
inset1.scatter( beta , fisher , marker='.'  )
inset1.grid()
majorLocator = plt.FixedLocator([0.985,0.99,0.999])
majorFormatter=plt.FormatStrFormatter('%.3f')
inset1.xaxis.set_major_locator(majorLocator)
inset1.xaxis.set_major_formatter(majorFormatter)
for tick in inset1.xaxis.get_major_ticks():
    tick.label.set_fontsize(9) 
    tick.label.set_rotation('vertical')
################"""
cax = fig.add_axes([0.88, 0.1, 0.02, 0.8])
cb=fig.colorbar(im1,cax)
cb.set_label('$log_{10}(N)$')

fig.savefig("fig1.eps",  facecolor='w', edgecolor='w', frameon=None)
plt.show()
