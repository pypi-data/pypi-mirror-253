# Chronos


![Build Status](https://img.shields.io/github/actions/workflow/status/h3x4g0ns/py-chronos/python-publish.yml)
[![PyPI version](https://badge.fury.io/py/py-quantize-chronos.svg)](https://badge.fury.io/py/py-quantize-chronos)

## About this Project

Python utility tool that takes in a function and outputs symbolic $O$ runtime.

## How it works

We basically take a couple known trajectories (specifically $O(1)$, $O(n)$, $O(n^2)$, $O(n^3)$, $O(\log{n})$, $O(n\log{n})$, $O(2^n)$ and we compute a least squares regression for each trajectory. We use a loss function to aggregate the differences and then return the trajectory with the smallest loss.

## Getting Started

### Prerequisites

You will need `numpy` and `tqdm` in order to use `chronos`. These should install as dependencies by default.

```sh
pip install py-quantize-chronos
```

## Usage

You need to pass in the name of the function you want timed into `timer`. The `timer` func will return the name of the function that models the runtime trajectory as a string. It also returns the coefficient that was outputted the least squares regression.

```py
import chronos

def fib_exp(n):
  if n <= 1:
    return n
  return fib_exp(n-1) + fib_exp(n-2)

print("running expoential runtime function")
func, coeff = chronos.timer(fib_exp, silent=True, num=100)
print(func, coeff, "\n")
```

In order for the analyis to work, the function's runtime must scale with respect to the input (ie. fibonacci sequence). Hence, the function must take an integer value. If the function doesn't support this, you must wrap the function in such a manner that the input's length can me modified with an integer.

```py
# original function
def counter(string: str):
  counter = 0
  for i in len(string):
    if i == "0":
      counter += 1
    return counter

# modified function to time
def wrapper(n: int):
  # generate random string with variable size
  letters = string.ascii_lowercase + string.digits
  inp = "".join(random.choices(letters, k=n))
  return counter(inp)
```

## Features to Add

Right now, the model is only able to support offline aysmptotic analysis. The goals is to perform online analysis so that we can utilize an `EARLY_STOP` if the last `k` predictions have been the same.

We would also like to support function that doesn't necesarily have integer inputs.

Furthermore, we need some more robust unit testing...

## Prior Attempts

In order to approximate asymptotic behavior, we use the second degree Taylor Expansion in order to estimate the trajectory of the runtime given the point. We retain a lookup table for the different asymptoics runtimes that we can expect (This included precomputing first and second derivatives). Following trajectories and their derivative functions are known:

$$ O(1), O(n), O(n^2), O(n^3), O(\log{n}), O(n\log{n}), O(2^n)$$

We can compare the second degree Taylor expansion for every known tracjectory. The formula for the second degree expansion is shown below.

$$T_2^f(x) = \sum_{n=0}^{2} \frac{f^{(n)}(x_0)}{n!} = g(x_0) + \frac{d}{dx}f(x_0)(x-x_0) + \frac{\frac{d^2}{dx^2}f(x_0)}{2}(x-x_0)^2$$

Where $g(x)$ is defined to be the measured runtime at timestep $x$.

We linearly scale the input to the test function and record its runtime. This new update is incorporated at the next time step to get a better approximation of the trajectory. Our optimization problem is defined to be as follows.

$$ \underset{f \in F}{\arg\min} \sum_1^{i=n}|T_n^f(i-i)(i)-g(i)|$$

Where $F$ is defined to be the set of all known trajectories to us, and $n$ is the number of data points we have.

> HOWEVER, the problem with this attempt is that if there are **large** or **small** coefficients present in our terms, they can artiically inflate or deflate the loss function. This leads to incorrect predictions with the asympotic analysis

## Helpful Links

- https://danielmuellerkomorowska.com/2020/06/02/smoothing-data-by-rolling-average-with-numpy/
- https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions.html
