import sys
import scipy.stats
import numpy as np
for line in sys.stdin:
    line=line.strip()
    fields=line.split()
    s1=[int(e) for e in fields[0:2]]
    s2=[int(e) for e in fields[2:4]]
    #print s1,s2
    a=np.array([s1,s2])
    #print a
    try:
        pval= scipy.stats.fisher_exact(a)[1]
        print pval
    except ValueError:
        print 1.0 
        print >>sys.stderr, float('NaN')
