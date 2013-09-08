import sys
import scipy.stats


def beta_mean(a,b):
    return a/(a+b)

def beta_mode(alpha,beta):
    return (alpha-1)/(alpha+beta-2)


for line in sys.stdin:
    line=line.strip()
    fields=line.split()
    nconv = float(fields[8])
    conv= float(fields[9])
    alpha=nconv+1
    beta=conv+1
    mean=beta_mean(alpha,beta)
    mode=beta_mode(alpha,beta)
    chrom=fields[0]
    pos=int(fields[1])
    methyl=float(fields[6])
    stddev_methyl=float(fields[7])
    met_beta=scipy.stats.beta( alpha , beta )
    p_gt_zero=1.0-met_beta.cdf(0.1) 
    print "a:%g b:%g %s:%d methyl:%g mean:%g mode:%g diff:%g p>0.1:%g"%\
    (alpha,beta,chrom,pos,methyl,mean,mode,mode-methyl,p_gt_zero)
