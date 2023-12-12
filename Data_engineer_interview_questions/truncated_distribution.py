import numpy as np
from scipy.stats import norm

def truncated_dist(m, sd, n, percentile_threshold):
    # Step 1: Calculate z-score for the given percentile threshold
    z_score = norm.ppf(percentile_threshold, loc=m, scale=sd)

    # Step 2: Generate a random sample from a normal distribution
    random_sample = np.random.normal(loc=m, scale=sd, size=n)

    # Step 3: Filter the sample to include only values below the z-score
    truncated_sample = [round(value,1) for value in random_sample if value <= z_score]

    return truncated_sample

# Example usage
m = 2
sd = 1
n = 6
percentile_threshold = 0.75
result = truncated_dist(m, sd, n, percentile_threshold)
print(result)




import numpy as np
import scipy.stats as st

def truncated_dist_2(m,sd,n,percentile_threshold):

    lim = st.norm(m,sd).ppf(percentile_threshold)
    r = np.random.normal(m, sd, n*2)[0:n*2]
    samples = [round(x,1) for x in r if x <= lim][0:n]
    return samples
    

m = 2
sd = 1
n = 6
percentile_threshold = 0.75
result = truncated_dist_2(m, sd,n, percentile_threshold)
print(result)