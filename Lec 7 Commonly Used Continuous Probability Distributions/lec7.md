# Lecture 7

3 topics:
1. Uniform Distribution
2. Normal Distribution
3. Exponential Distribution(compare & contrast with Poisson Distribution)

## 1 : Uniform Distribution


## 2 : Normal Distribution


## 3 : Exponential Distribution
Used to measure the time between events// time elapsed before event occurs
- continuous on an interval
- lambda = rate parameter = 1/mean = 1/expected value = average number of events per unit time
- E[X] = 1 / lambda
- PDF: f(x) = lambda * exp(-lambda * x) for x >= 0
- E[X] = integral from 0 to infinity of x * f(x) dx = 1 / lambda
- Var[X] = 1 / lambda^2 = E[X^2] - (E[X])^2, by definition of variance
- SD[X] = 1 / lambda
P(a <= X <= b) = integral from a to b of f(x) dx = exp(-lambda * a) - exp(-lambda * b)
P(X>x) = integral from x to infinity of f(x) dx = exp(-lambda * x)
P(X<=x) = integral from 0 to x of f(x) dx = 1 - exp(-lambda * x)
![Photo of Poisson Distribution vs Exponential Distribution](/images/"poisson dist vs exp.png")