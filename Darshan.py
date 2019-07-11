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
    Astring = string.lower()
    x = list(range(len(Astring)))
    random.shuffle(x)
    newString = ""
    for item in x:
        newString += Astring[item]
    if(string[0].isupper()):
        newString = newString.capitalize()
    return newString



