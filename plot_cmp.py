import matplotlib.pylab as plt
import numpy as np
data=np.genfromtxt("cmp_results.txt",dtype=None)

fig,ax=plt.subplots()
fig.patch.set_visible(False)
#ax.patch.set_visible(False)
ax.set_xlim(0.0,1)
ax.set_ylim(0,1)
ax.grid(True,which='major')
ax.scatter(data[:,0],data[:,1],c='r',marker='o',edgecolor='none')
ax.set_xlabel(r"$P\,(X_1>X_2)$")
ax.set_ylabel(r"Fisher's p value")

ax2=fig.add_axes([0.3,0.3,0.3,0.3])
#ax2.patch.set_visible(False)
fcut=0.05
ax2.set_ylim(1.0e-6,fcut)
idx_zoom=data[:,1]<=fcut
xzoom=data[idx_zoom,0]
yzoom=data[idx_zoom,1]
#ax2.set_xscale('log')
#ax2.set_yscale('log')
ax2.scatter(xzoom,yzoom,c='r',marker='o',edgecolor='none')


plt.show()
