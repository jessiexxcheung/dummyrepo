import random

name = "Darshan"
def fun(string):
    """

    Parameters
    ----------
    string: A string that is inputted by the user.

    Returns
    -------
    newString: The same string but the characters are in random order.

    """
    string = string.lower()
    x = list(range(len(string)))
    random.shuffle(x)
    newString = ""
    for item in x:
        newString += string[item]
    return newString



