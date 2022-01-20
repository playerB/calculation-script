import numpy as np
import pandas as pd
from scipy import stats
import sys
import math

def main(AQL, LTPD, alpha, beta):
    table = pd.DataFrame()
    np1 = 0
    np2 = 0
    for i in np.arange(0,10,1): # c range 0-10
        for j in np.arange(0,10,0.01): # find np1
            num1 = stats.poisson.cdf(k=i, mu=j)
            if (num1 < 1-alpha):
                np1 = j-0.01
                break
        for k in np.arange(0,20,0.01): # find np2
            num2 = stats.poisson.cdf(k=i, mu=k)
            if (num2 < beta) :
                np2 = k-0.01
                break
        table = table.append(pd.DataFrame([[i, np1, np2, (np2/np1), num1, num2]], columns=['c','np1','np2', 'p2/p1','cdf1', 'cdf2']), ignore_index=True)
    print("At alpha={0}, beta={1}".format(alpha, beta))
    print(table, '\n')

    fourcase = pd.DataFrame()
    c1 = 0
    c2 = 0
    for row in table.iterrows():
        if (row[1]['p2/p1'] < LTPD/AQL):
            c1 = table.loc[row[0]-1, 'c']
            c2 = table.loc[row[0], 'c']
            print(table.loc[c1, 'c'], table.loc[c1, 'p2/p1'])
            print(table.loc[c2, 'c'], table.loc[c2, 'p2/p1'])
            break
    n1 = math.ceil(table.loc[c1, 'np1']/AQL)
    n2 = math.ceil(table.loc[c1, 'np2']/LTPD)
    n3 = math.ceil(table.loc[c2, 'np1']/AQL)
    n4 = math.ceil(table.loc[c2, 'np2']/LTPD)
    fourcase = fourcase.append(pd.DataFrame([[c1, n1, alpha, stats.poisson.cdf(k=c1, mu=n1*LTPD), abs(stats.poisson.cdf(k=c1, mu=n1*LTPD)-beta)]], columns=['c','n','alpha','beta', 'diff']), ignore_index=True)
    fourcase = fourcase.append(pd.DataFrame([[c1, n2, 1-stats.poisson.cdf(k=c1, mu=n2*AQL), beta, abs((1-stats.poisson.cdf(k=c1, mu=n2*AQL))-alpha)]], columns=['c','n','alpha','beta', 'diff']), ignore_index=True)
    fourcase = fourcase.append(pd.DataFrame([[c2, n3, alpha, stats.poisson.cdf(k=c2, mu=n3*LTPD), abs(stats.poisson.cdf(k=c2, mu=n3*LTPD)-beta)]], columns=['c','n','alpha','beta', 'diff']), ignore_index=True)
    fourcase = fourcase.append(pd.DataFrame([[c2, n4, 1-stats.poisson.cdf(k=c2, mu=n4*AQL), beta, abs((1-stats.poisson.cdf(k=c2, mu=n4*AQL))-alpha)]], columns=['c','n','alpha','beta', 'diff']), ignore_index=True)
    print(fourcase)

if __name__ == "__main__":
    if (len(sys.argv) == 5):
        main(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
    else:
        print("Usage: $ singlesp.py <AQL> <LTPD> <alpha> <beta>")