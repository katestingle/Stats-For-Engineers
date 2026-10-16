"""
Background
Use the exponential distribution when you want to measure
the time between events in a Poisson process.

poisson dist: how many times in an interval (discrete)
- poisson uses lambda, the average number of events per interval
- examples: # of customer support calls received in 1 hr. # of typos on a page of a book

exponential dist: how much time passes before next event (continuous)
- lambda = rate parameter = average rate of events
- 1 / lambda = mean time between events
 - examples: how long a customer waits in line b4 being serve. how many hours a phone battery lasts before dying
 - time until a lightbulb burns out

 how do they tie together?
 Both describe a Poisson process:
 1. evts happen INDEPENDENTLY at a constant average rate lambda
 2. the count of evts in a time windows follows a poissions distribution
 3. the time you wait until the very first evet occurs follow an exponential distribution
 ** the lambdas are the same for both distributions **
"""

from scipy.stats import expon

scale_param = 2.0  # 1 / lambda

# 1. Probability that a bus arrives in exactly 3 minutes (PDF)
pdf_val = expon.pdf(3, scale=scale_param)
print(f"PDF at 3 mins: {pdf_val:.4f}")

# 2. Probability of waiting 3 minutes or LESS (CDF)
cdf_val = expon.cdf(3, scale=scale_param)
print(f"Probability of waiting ≤ 3 mins: {cdf_val:.4f}")

# 3. Probability of waiting MORE than 5 minutes (SF)
sf_val = expon.sf(5, scale=scale_param)
print(f"Probability of waiting > 5 mins: {sf_val:.4f}")

# 4. Find the median waiting time (50th percentile / PPF)
median_wait = expon.ppf(0.5, scale=scale_param)
print(f"Median waiting time: {median_wait:.2f} minutes")
