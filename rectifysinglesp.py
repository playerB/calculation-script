import pandas as pd
import numpy as np
from scipy import stats
import math
import sys

def main(AOQL,N,p):
    table = pd.DataFrame(columns=['c','y','n','Pa','ATI'])
    ylist = [0.3679,0.8408,1.371,1.942,2.544,3.168,3.812,4.472,\
        5.146,5.831,6.528,7.233,7.948,8.670,9.398,10.13,10.88, \
        #11.62,12.37,13.13,13.89,14.66,15.43,16.20,16.98,17.78, \
        #18.54,19.33,20.12,20.91,21.70,22.50,23.30,24.10,24.90, \
        #25.71,26.52,27.33,28.14,28.96,29.77
        ]
    clist = np.arange(0,17,1)
    table['c'] = clist
    table['y'] = ylist
    nlist = list(map(lambda y: round((y*N)/(N*AOQL+y),0), ylist))
    table['n'] = nlist
    Palist = list(map(lambda c,n: round(stats.poisson.cdf(k=c, mu=n*p),3), clist, nlist))
    table['Pa'] = Palist
    ATIlist = list(map(lambda Pa,n: round((n+(1-Pa)*(N-n)),0), Palist, nlist))
    table['ATI'] = ATIlist
    print(table)
    res = table.loc[table['ATI'] == table['ATI'].min()]
    print("\n\nmin ATI, (n, c) : {} ({}, {})".format(math.floor(res['ATI'].values[0]), math.floor(res['n'].values[0]), res['c'].values[0]))

if __name__ == '__main__':
    main(float(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))