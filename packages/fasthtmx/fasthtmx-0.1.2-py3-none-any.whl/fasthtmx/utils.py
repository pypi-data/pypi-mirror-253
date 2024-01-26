import os


def getFilePath(dunder_file: str):
    """
    Returns the absolute path of a file.
    Parameters:
    - dunder_file (str): The __file__ dunder variable.
    """
    return os.path.dirname(os.path.realpath(dunder_file))
