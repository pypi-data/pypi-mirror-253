# TODO: import necessary libraries

from .Generaldistribution import Distribution
import math
import matplotlib.pyplot as plt


""" Binomial distribution class for calculating and 
visualizing a Binomial distribution.

Attributes:
    mean (float) representing the mean value of the distribution
    stdev (float) representing the standard deviation of the distribution
    data_list (list of floats) a list of floats to be extracted from the data file
    p (float) representing the probability of an event occurring
            
"""  

class Binomial(Distribution):
        
    def __init__(self, prob, size):
        
        self.p = prob
        
        self.n = size
        
        mean = self.calculate_mean()
        
        stdev = self.calculate_stdev()
        
        Distribution.__init__(self, mean, stdev)
    
    def calculate_mean(self):
        
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        
        
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args: 
            None

        Returns: 
            float: the p value
            float: the n value

        """
        
        self.n = len(self.data)
        self.p = sum(self.data)/self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev() 
        
        return self.p, self.n
        
    def plot_bar(self):
    
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        
    
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        a = math.factorial(self.n) / (math.factorial(self.n - k) * math.factorial(k))
        b = (self.p**k) * ((self.p-1)**self.n-k)
        return a * b
        
    # write a method to plot the probability density function of the binomial distribution
    def plot_bar_pdf(self, n_spaces = 50):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
    
        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n
        
        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.
        
        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists
        
        min_range = min(self.data)
        max_range = max(self.data)
        
        interval = 1.0 * (max_range - min_range)/n_spaces
        
        x = []
        y = []
        
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))
            
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Binomial Distribution')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
    
    def __add__(self, other):  
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        result = Binomial()
        
        result.n = self.n + other.n
        result.p = self.p
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)