from matplotlib import pyplot 
import numpy as np

def true_function():
    """
    >>> true_function(0)
    0
    """
    #y = sin(pi * x * 0.8) * 10
    x = np.arange(-1,1,0.01)
    pyplot.plot(x, y(x),label="sin")
    pyplot.legend()
    pyplot.show()

def y(x):
    return np.sin(np.pi * x * 0.8) * 10

if __name__ == '__main__':
    """
    import doctest
    doctest.testmod()
    """
    true_function()
