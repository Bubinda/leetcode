import numpy as np
import seaborn as sns

N = 10_000

def norm_dist_hist(N):
    # Generating Random normal distribution samples
    x = np.random.randn(N)
    # Plotting histogram    
    sns.histplot(x, bins = 20, kde=True);
    return x
   
X = norm_dist_hist(N)