import sys
import numpy as np
import matplotlib 
import pandas as pd

names=["nc1","c1","nc2","c2","pval"]

try:
    p_file=sys.argv[1]
    n_file=sys.argv[2]
except:
    sys.stderr.write("usage:<p> <n>")
    sys.exit(1)

p_data=pd.read_csv(p_file,header=None,sep=" ",names=names)
n_data=pd.read_csv(n_file,header=None,sep=" ",names=names)

for thr in [1e-1,5e-2,2e-2,1e-2,5e-3,2e-3,1e-3]:
    fp = len (n_data[n_data['pval'] < thr])
    fn = len(p_data[p_data['pval'] >= thr])
    tp = len(p_data[p_data['pval'] <thr ]) 
    tn = len(n_data[n_data['pval']>=thr ])
    try:
        fpr = float(fp) / ( fp + tn )
        tpr = float(tp) /  (tp + fn   )
    except ZeroDivisionError:
        print "warning:",thr,fp, tn, tp, fn
    sys.stderr.write("thr=%g fp=%d fn=%d tp=%d tn=%d\n"%(thr,fp,fn,tp,tn))
    print thr,fpr,tpr
