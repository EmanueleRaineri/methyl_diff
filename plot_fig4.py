import numpy as np
import matplotlib.pylab as plt
import sys
import pandas as pd
from scipy.stats import gaussian_kde


def prepare_data(data,begin,end):
    data=data.dropna()
    data=data[(data[0]>=begin) & (data[0]<=end)]
    return data

def split_data(data,col):
    data_bottom=data[data[col]<0.5]
    data_mid=data[data[col]==0.5]
    data_top=data[data[col]>0.5]
    return (data_bottom, data_mid , data_top) 

dir="/home/emanuele/cluster/non_cpg"
data10000=pd.read_csv(dir+"/G199.G202.chr1.diff.in.10000",header=None,sep=" ")
data=pd.read_csv(dir+"/G199.G202.chr1.diff.in.slice",header=None,sep=" ")



data10000=prepare_data(data10000,6e7,9e7)
print data10000
[data10000_bottom,data10000_mid, data10000_top]=\
split_data(data10000,4)

fig = plt.figure(frameon=False, figsize=( 10 , 6 ) )
fig.patch.set_visible(False)
ax = fig.add_subplot(121)
ax.scatter(data10000_top[0],data10000_top[4],marker='.',color='green')
ax.scatter(data10000_bottom[0],data10000_bottom[4],marker='.',color='red')
ax.scatter(data10000_mid[0],data10000_mid[4],marker='.',color='black')

ax = fig.add_subplot(122)
data = prepare_data(data,1e8,1.00001e8)
print data
[dbottom,dmid,dtop] = split_data(data,1)
ax.scatter(dbottom[0],dbottom[1],marker='.',color='red')
ax.scatter(dtop[0],dtop[1],marker='.',color='green')



fig.savefig("fig4.eps",  facecolor='w', edgecolor='w', frameon=None)

plt.show()
