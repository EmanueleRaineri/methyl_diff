import scipy.stats
import numpy as np
import matplotlib.pylab as plt
import sys
import pandas as pd



#a,b=[int(e) for e in sys.argv[1:]]
#print a,b

def generate_beta_from_reads(unconv,conv):
    a=unconv+1
    b=conv+1
    met_beta=scipy.stats.beta( a , b )
    x=np.linspace(0,1,1000,endpoint=True)
    y=[met_beta.pdf(e) for e in x]
    return (x,y)


def std_beta_of_reads(unconv,conv):
    a=float(unconv+1)
    b=float(conv+1)
    return np.sqrt(a*b/((a+b)**2*(a+b+1)))

def mean_beta_of_reads(unconv,conv):
    a=float(unconv+1)
    b=float(conv+1)
    return a/(a+b)

def mode_beta_of_reads(unconv,conv):
    a=float(unconv+1)
    b=float(conv+1)    
    return (a-1)/(a+b-2)

fig = plt.figure( frameon=False,
    figsize=( 10 , 6 ) 
    )
fig.patch.set_visible(False)

ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
#
a1=1;b1=3
a2=20;b2=30
x1 , y1 = generate_beta_from_reads( a1 , b1 )
x2 , y2 = generate_beta_from_reads( a2 , b2 )
mean1=mean_beta_of_reads(a1,b1)
mean2=mean_beta_of_reads(a2,b2)
mode1=mode_beta_of_reads(a1,b1)
mode2=mode_beta_of_reads(a2,b2)
std1=std_beta_of_reads(a1,b1)
std2=std_beta_of_reads(a2,b2)
print "mean1=%g,mode1=%g,sd1=%g,mean2=%g,mode2=%g,sd2=%g"%\
(mean1,mode1,std1,mean2,mode2,std2)
#
a3,b3=(10,10)
a4,b4=(2,18)
x3 , y3 = generate_beta_from_reads(a3,b3)
x4 , y4 = generate_beta_from_reads(a4,b4)
#
ax1.plot(x1,y1,color="blue",label="%d,%d"%(a1,b1),lw=2)
ax1.plot(x2,y2,color="green",label="%d,%d"%(a2,b2),lw=2)
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles, labels)
ax1.vlines([mode1],0,
    np.max(y1),
    color="blue",lw=2,linestyle="dashed")
ax1.vlines([mode2],0,
    np.max(y2),
    color="green",lw=2,linestyle="dashed")
#
ax2.plot(x3,y3,color="blue",label="%d,%d"%(a3,b3),lw=2)
ax2.plot(x4,y4,color="green",label="%d,%d"%(a4,b4),lw=2)
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels)
#
fig.savefig("fig4.eps",  facecolor='w', edgecolor='w', frameon=None)
plt.show()
