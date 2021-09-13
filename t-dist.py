import sys
from scipy import stats
# t-distribution calculator for critical values
# https://en.wikipedia.org/wiki/Student%27s_t-distribution
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html
def t_dist(n, n_critical):
    # n = degrees of freedom
    # n_critical = critical value
    # returns the t_critical for tail p-value of n_critical
    return stats.t.ppf(n_critical, n)

def t_dist_p(n, t_critical):
    # n = degrees of freedom
    # t_critical = critical value
    # returns the p-value for t(X>t_critical)
    return stats.t.cdf(t_critical, n)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print("\n t-critical =", t_dist(int(sys.argv[1]), 1-float(sys.argv[2])) , "\n")
    elif len(sys.argv) == 4 and sys.argv[3] == "p":
        print("\n p-value =", 1-t_dist_p(int(sys.argv[1]), float(sys.argv[2])) , "\n")
    else:
        print("Usage: t-dist.py <df1> <p-value> \n or\n t-dist.py <df1> <t-stat> p")