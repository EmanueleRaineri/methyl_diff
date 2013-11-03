import sys
import scipy.stats


cov1 , p1 , cov2, p2, size = [float(e) for e in sys.argv[1:]]
size=int(size)
"""beta1=scipy.stats.beta( a1 , b1 )
beta2=scipy.stats.beta( a2 , b2 )"""
binom1=scipy.stats.binom(cov1,p1)
binom2=scipy.stats.binom(cov2,p2)

for i in range(size):
    nc1=binom1.rvs()
    c1=int(cov1-nc1)
    nc2=binom2.rvs()
    c2=int(cov2-nc2)
    print nc1 , c1 , nc2, c2 

