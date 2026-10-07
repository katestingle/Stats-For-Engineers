import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

print(binom.pmf(5, 10, 0.5)) # Evaluate the Binomial(n=10,p=0.5) p.m.f. at x=5. This will give P(X=5)
print(binom.cdf(5, 10, 0.5)) # Evluate the Binomial(n=10,p=0.5) c.d.f. at x=5. This will give P(X<=5)

# Parameters
n = 10
p = 0.5

# Values of k (number of successes)
k_values = np.arange(0, n + 1)

# PMF for each k
pmf_values = binom.pmf(k_values, n, p)

# Plotting
plt.bar(k_values, pmf_values, color='skyblue')
plt.xlabel('Number of successes (k)')
plt.ylabel('Probability')
plt.title('Binomial Distribution PMF: n=10, p=0.5')
plt.grid(True)
plt.show()

# Now let us create the same graph for Binomial(n=10,p=0.8) distribution.
# As you will see below, since success probability has increased, larger outcomes of X are more likely.
# Parameters
n = 10
p = 0.8

# Values of k (number of successes)
k_values = np.arange(0, n + 1)

# PMF for each k
pmf_values = binom.pmf(k_values, n, p)

# Plotting
plt.bar(k_values, pmf_values, color='skyblue')
plt.xlabel('Number of successes (k)')
plt.ylabel('Probability')
plt.title('Binomial Distribution PMF: n=10, p=0.8')
plt.grid(True)
plt.show()