import sys
import scipy.stats
import scipy.special
import numpy as np

def mean_var_beta(alpha,beta):
    m = float(alpha)/(alpha+beta)
    v = float(alpha*beta)/((alpha+beta)**2*(alpha+beta+1))
    return (m,v) 

sqrt2=np.sqrt(2)

for line in sys.stdin:
    line=line.strip()
    fields=line.split()
    nc1,c1,nc2,c2=[int(e) for e in fields]
    alpha1=nc1+1;beta1=c1+1
    alpha2=nc2+1;beta2=c2+1
    m1,v1=mean_var_beta(alpha1,beta1)
    m2,v2=mean_var_beta(alpha2,beta2)   
    z_score=(m1-m2)/np.sqrt(v1+v2)
    #if (z_score>0):
    pval = 1 - 0.5*(1+scipy.special.erf(z_score/sqrt2))
    #else:
     #   pval = 0.5*(1+scipy.special.erf(z_score/sqrt2))
    print z_score,pval
