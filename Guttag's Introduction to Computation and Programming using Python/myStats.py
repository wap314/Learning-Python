X =[]

def variance(X):
    """Assumes that X is a list of numbers.
       Return the variance of X."""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    return tot/len(X)

def stdDev(X):
    """Assumes that X is a list of numbers.
       Return the standard deviation of X."""
    return variance(X)**0.5