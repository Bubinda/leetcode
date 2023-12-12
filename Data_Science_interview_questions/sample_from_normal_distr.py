import numpy as np
import matplotlib.pyplot as plt

def generate_and_plot_normal_distribution(N):
    # Generate N samples from a normal distribution with mean 0 and standard deviation 1
    samples = np.random.normal(0, 1, N)
    
    # Plot the histogram
    plt.hist(samples, bins=30, density=True, alpha=0.7, color='blue')
    plt.title(f'Normal Distribution - {N} Samples')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    # Show the plot (you can omit this if you just want to generate data without plotting)
    plt.show()

# Example usage:
# Set the number of samples (N) you want
N = 1000

# Call the function to generate and plot N samples
generate_and_plot_normal_distribution(N)



# same with scipy.stats.norm

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_and_plot_normal_distribution(N):
    # Generate N samples from a normal distribution with mean 0 and standard deviation 1
    samples = norm.rvs(loc=0, scale=1, size=N)
    
    # Plot the histogram
    plt.hist(samples, bins=20, density=True, alpha=0.7, color='blue')
    plt.title(f'Normal Distribution - {N} Samples')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    
    # Show the plot (you can omit this if you just want to generate data without plotting)
    plt.show()

# Example usage:
# Set the number of samples (N) you want
N = 1000

# Call the function to generate and plot N samples
generate_and_plot_normal_distribution(N)
