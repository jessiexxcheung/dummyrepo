name = "Emily"

def factorial(x):
    '''
    Finds the factorial of a number
    Parameters
    ----------
    x: int
    Positive number to find a factorial of
    Returns
    -------
    int
    The factorial of x
    '''
    if x == 0 or x == 1:
        return 1

    else:
        return x*factorial(x-1)