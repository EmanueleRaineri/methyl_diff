import sys
import scipy.stats


a1,b1,a2,b2=[int(e) for e in sys.argv[1:]]
beta1=scipy.stats.beta( a1 , b1 )
beta2=scipy.stats.beta( a2 , b2 )

size=10000

c=0
for i in range(size):
    if (beta1.rvs()>=beta2.rvs()):
        c=c+1

print float(c)/size
