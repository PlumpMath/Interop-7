#!/bin/python
import matplotlib
import numpy as np
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


Laner = range(1,int(LC)+1)
gth = np.arange(int(LC))
Alignment = np.array(Aligns[1:]).astype(np.float)
Q30 = np.array(Q30s[1:]).astype(np.float)
Density = np.array(Densities[1:]).astype(np.float)
Cluster = np.array(Clusters[1:]).astype(np.float)
Pass = np.array(PFs[1:]).astype(np.float)
Total = np.array(Totals[1:]).astype(np.float)
##pdf generation
with PdfPages(FCID+".pdf")as pdf:
    grid_size = (6,2)
    #alignment
    plt.subplot2grid(grid_size,(1,0), rowspan=2, colspan =1)
    plt.bar(gth,Alignment)
    plt.ylabel('Percent')
    plt.xticks(gth,Laner)
    plt.yticks(np.arange(0,2,.2))
    plt.plot((-1,2),(0.8,0.8),'k--')
    plt.plot((-1,2),(1.2,1.2), 'k--')
    plt.title('Alignment')
    #Q30
    plt.subplot2grid(grid_size,(1,1), rowspan=2, colspan =1)
    plt.bar(gth,Q30)
    plt.ylabel('Percent')
    plt.xticks(gth,Laner)
    plt.yticks(np.arange(0,101,20))
    plt.title('Q30')
    #Density
    plt.subplot2grid(grid_size,(3,0), rowspan=2, colspan =1)
    plt.bar(gth,Density)
    plt.ylabel('Percent')
    plt.xticks(gth,Laner)
    plt.yticks(np.arange(0,101,20))
    plt.title('Clusters Pass Filter')
    #Cluster
    plt.subplot2grid(grid_size, (3,1),rowspan=2, colspan =1)
    plt.bar(gth,Cluster)
    plt.ylabel('K/mm^2')
    plt.xticks(gth,Laner)
    plt.title('Cluster Density')
    plt.yticks(np.arange(0,1200,200))
    plt.tight_layout()
    pdf.savefig()
    plt.close()