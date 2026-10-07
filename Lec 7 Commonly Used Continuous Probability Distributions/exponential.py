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
