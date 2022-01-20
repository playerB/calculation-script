import pandas as pd
import numpy as np
from scipy import stats
import sys

def main(n1,c1,n2,c2,p):
    Pa1 = round(stats.poisson.cdf(k=c1, mu=n1*p), 3)
    Pr1 = round(1-stats.poisson.cdf(k=c2, mu=n1*p), 3)


    table = pd.DataFrame(columns=['x1', 'Px1, n1p', 'x2', 'Pxa2, n2p', 'Pxr2, n2p'])
    table['x1'] = np.arange(c1+1, c2+1)
    table['Px1, n1p'] = stats.poisson.cdf(k=table['x1'], mu=n1*p) - stats.poisson.cdf(k=table['x1']-1, mu=n1*p)
    for i in range(c1+1, c2+1):
        list = np.arange(c2 - i, -1, -1)
        table.loc[i - c1 - 1, 'x2'] = str(list)
        table.loc[i - c1 - 1, 'Pxa2, n2p'] = round(stats.poisson.cdf(k=c2 - i, mu=n2*p), 3)
    table['Pxr2, n2p'] = 1 - table['Pxa2, n2p']
    print(table, "\n")

    print("P(A1) = ", Pa1, "P(R1) = ", Pr1)
    Pa2 = (table['Pxa2, n2p'] * table['Px1, n1p']).sum()
    Pr2 = (table['Pxr2, n2p'] * table['Px1, n1p']).sum()
    print("P(A2) = ", round(Pa2, 3), "P(R2) = ", round(Pr2, 3))
    Pa = round(Pa1 + Pa2, 3)
    Pr = round(Pr1 + Pr2, 3)
    print("P(A) = ", Pa, "P(R) = ", Pr)
    ASN = n1 + n2 *(Pa2 + Pr2)
    print("ASN = ", round(ASN, 0))

if __name__ == "__main__":
    if len(sys.argv) == 6:
        main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]))
    else:
        print("Usage: python3 doublesp.py n1 c1 n2 c2 p")
        