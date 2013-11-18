import numpy as np
import matplotlib.pylab as plt


def histo_2d(ax,x,y,xlabel,ylabel):
    im=ax.hexbin(x,y,bins='log')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return im 

data = np.genfromtxt( "G199.G202.beta.fisher.zscore" , dtype=None )

print data[0]

beta   =[e[11] for e in data]
fisher =[e[12] for e in data]
z      =[e[13] for e in data]

print beta[0],fisher[0],z[0]

fig=plt.figure(frameon=False)
ax1 = fig.add_axes([0.1,0.1,0.35,0.8]) 
ax2 = fig.add_axes([0.50,0.1,0.35,0.8]) 
ax2.yaxis.set_major_locator(plt.NullLocator())
#fig.tight_layout()
im1 = histo_2d( ax1,beta,fisher,"Beta","Fisher's test $p$-value" )
im2 = histo_2d( ax2,beta,z,"Beta","$Z$ score $p$-value" )
#cax = fig.add_subplot(133)
cax = fig.add_axes([0.88, 0.1, 0.02, 0.8])
cb=fig.colorbar(im1,cax)
cb.set_label('$log_{10}(N)$')

fig.savefig("fig1.eps",  facecolor='w', edgecolor='w', frameon=None)
plt.show()
