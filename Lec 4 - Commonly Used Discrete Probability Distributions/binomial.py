from scipy.stats import binom
x = 5
n = 15
p = 0.4

# Computes the probability mass function (PMF)
pmf = binom.pmf(x,n,p)
print(pmf)

# Computes the cumulative distribution function (CDF)
cdf = binom.cdf(x, n, p)
print(cdf)

# Generates m random Binomial-distributed values
m = 2
random_vals = binom.rvs(n,p,size = m)
print(random_vals)

# Computes the quantile associated with probability q
q = 0.2
quantile = binom.ppf(q,n,p)
print(quantile)

