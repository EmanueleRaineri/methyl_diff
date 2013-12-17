import sys
import numpy as np
import matplotlib 

"""compute_power_beta"""

try:
    p_file=sys.argv[1]
    n_file=sys.argv[2]
except:
    sys.stderr.write("usage:<p> <n>")
    sys.exit(1)


p_data = np.genfromtxt( p_file )
n_data = np.genfromtxt( n_file ) 

for thr in [0.5,0.6,0.7,0.8,0.9,0.95,0.99]:


    fp = len(n_data[n_data >= thr])
    fn = len(p_data[p_data < thr])
    tp = len(p_data[p_data >=thr ]) 
    tn = len(n_data[n_data< thr ]) 
    #tp = len(tp_data)
    #tn = len(tn_data)
    try:
        fpr = float(fp) / ( fp + tn )
        tpr = float(tp) /  (tp + fn   )
    except ZeroDivisionError:
        print "warning:",thr,fp, tn, tp, fn
    
    sys.stderr.write("thr=%g fp=%d fn=%d tp=%d tn=%d\n"%(thr,fp,fn,tp,tn))
    print thr,fpr,tpr
