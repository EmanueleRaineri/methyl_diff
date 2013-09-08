import sys
import scipy.stats
import scipy.special

a1,b1,a2,b2=[int(e) for e in sys.argv[1:]]
beta1=scipy.stats.beta( a1 , b1 )
beta2=scipy.stats.beta( a2 , b2 )



def h(a1,b1,a2,b2):
    beta=scipy.special.beta
    return beta(a1+a2,b1+b2)/(beta(a1,b1)*beta(a2,b2))

def g(a1,b1,a2,b2):
    if (a1==b1==a2==b2):
        return 0.5
    if (a1>1):
        return g(a1-1,b1,a2,b2)+h(a1-1,b1,a2,b2)/(a1-1)
    if (b1>1):
        return g(a1,b1-1,a2,b2)-h(a1,b1-1,a2,b2)/(b1-1)
    if (a2>1):
        return g(a1,b1,a2-1,b2) - h(a1,b1,a2-1,b2)/(a2-1)
    if (b2>1):
        return g(a1,b1,a2,b2-1) + h(a1,b1,a2,b2-1)/(b2-1)

print g(a1,b1,a2,b2)
