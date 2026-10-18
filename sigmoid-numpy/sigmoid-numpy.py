import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x = np.asarray(x)
    # return 1/(1 + np.exp(-x))
    
    # if x becomes to small (like -10000 : which is like exp ^ 1000 ; very large), we may run into issue called Runtime overflow. to avoid this we use:

    return np.where(x>=0, 
                    1/(1 + np.exp(-x)),  # Standard formula for positive values
                    np.exp(x)/(1 + np.exp(x))) # Algebraically identical version for negative values
    
    