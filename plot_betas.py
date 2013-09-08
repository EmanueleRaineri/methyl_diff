import matplotlib.pylab as plt
import numpy as np
import scipy.stats
import sys

a,b=[int(e) for e in sys.argv[1:]]
print a,b

met_beta=scipy.stats.beta( a , b )
x=np.linspace(0,1,1000,endpoint=True)
y=[met_beta.pdf(e) for e in x]
fig,ax=plt.subplots()
ax.plot(x,y)
plt.show()

