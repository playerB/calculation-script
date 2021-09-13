import sys
from scipy import stats
# F-distribution calculator for critical values
# https://en.wikipedia.org/wiki/F-distribution
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html
def f_dist(m, n, n_critical):
    # n = number of samples (df2)
    # m = number of variables (df1)
    # n_critical = critical value
    # returns the F_critical value for tail p-value of F(X>n_critical)
    return stats.f.ppf(n_critical, m, n)

def f_dist_p(m, n, n_critical):
    # n = number of samples (df2)
    # m = number of variables (df1)
    # n_critical = critical value
    # returns the p-value of F(X>n_critical)
    return stats.f.cdf(n_critical, m, n)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        print("\n F-critical =", f_dist(int(sys.argv[1]), int(sys.argv[2]), 1-float(sys.argv[3])) , "\n")
    elif len(sys.argv) == 5 and sys.argv[4] == "p":
        print("\n p-value =", 1-f_dist_p(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])) , "\n")
    else:
        print("Usage: f-dist.py <df1> <df2> <p-value> \n or\n f-dist.py <df1> <df2> <f-stat> p")