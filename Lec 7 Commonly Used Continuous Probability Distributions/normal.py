# Normal Distribution
# f(x; mean, std) = exp(-0.5 * ((x - mean) / std)^2) / (std * sqrt(2*pi))
from scipy.stats import norm

x = float(input("Enter the value of x to find the Probability Density at: "))
loc = float(input("Enter the mean of x for the PDF: "))
scale = float(input("Enter the standard deviation of x for the PDF: "))

print(norm.pdf(x, loc=loc, scale=scale))  # Computes the probability density function (PDF)
print(norm.cdf(x, loc=loc, scale=scale))  # Computes the cumulative distribution function (CDF)

size = int(input("Enter the size of the random sample: "))
rand_norm = norm.rvs(loc=loc, scale=scale, size=size)  # Generates random numbers from a Normal distribution
print("These are the random numbers generated from the gaussian distribution of size:", size)
print(rand_norm)

p = float(input("Enter the value of p to find the quantile at: "))
print(norm.ppf(p, loc=loc, scale=scale))  # Computes quantiles (inverse CDF)
