import sys
import numpy as np
import matplotlib 

"""compute_power_beta"""

try:
    tp_file=sys.argv[1]
    tn_file=sys.argv[2]
except:
    sys.stderr.write("usage:<tp> <tn>")
    sys.exit(1)


tp_data = np.genfromtxt( tp_file )
tn_data = np.genfromtxt( tn_file ) 

for thr in [0.5,0.6,0.7,0.8,0.9,0.95,0.99]:


    fp = len (tn_data[tn_data >= thr])
    fn = len(tp_data[tp_data < thr])
    tp = len(tp_data)
    tn = len(tn_data)
    try:
        fpr = float(fp) / ( fp + tn )
        tpr = float(tp) /  (tp + fn   )
    except ZeroDivisionError:
        print "warning:",thr,fp, tn, tp, fn

    print thr,fpr,tpr
