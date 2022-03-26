import pandas as pd

def get_csv_data(path):
    """
    This function takes a path to a csv file and returns a pandas dataframe
    
    :param path: the path to the CSV file
    :return: A dataframe
    """
    return pd.read_csv(path)

def summer(first, second):
    """
    Add two numbers together
    
    :param first: The first number in the addition
    :param second: The second number to add
    :return: The sum of the two numbers.
    """
    return first + second

