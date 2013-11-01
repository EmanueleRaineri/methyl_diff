import matplotlib.pylab as plt
import matplotlib as mpl
import numpy as np

data=np.genfromtxt("G199.G202.beta.fisher.chr1.subsample",dtype=None)

fisher = [e[12] for e in data]
beta =   [e[11] for e in data]

h,ex,ey=np.histogram2d(fisher,beta)
print np.min(h) , np.max(h)

print np.shape(h)

hf=np.reshape(h,(100))

# now the colormap magic begins


cmap =  mpl.cm.cool
#cmap.set_over('0.25')
#cmap.set_under('1000')
#bounds = [10,20,50,100,200,500,1000]
norm = mpl.colors.LogNorm(vmin = np.min(h) , vmax = np.max(h))
ax=plt.hexbin( fisher, beta, bins="log" )
cb=plt.colorbar()
cb.set_label('$log_{10}(N)$')
ax=plt.gca()
ax.set_xlabel("Fisher's test pvalue")
ax.set_ylabel("$P(X_1>X_2)$")
#ax=fig.add_axes([0., 10, 0, 10])
#cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm)


plt.show()

