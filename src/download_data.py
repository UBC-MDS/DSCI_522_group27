import pandas as pd
import os

def download_data(data_folder, filename):
    """Function for downloading the raw white wine quality data and saving as a .csv file

    Parameters:
    data_folder (str): data directory
    filename (str): name data file should be saved as

    Returns:
    
    Example:
    download_data('data','raw_data.csv')

   """
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    data = pd.read_csv(url, sep=';')
    if not os.path.isdir(data_folder):
        os.mkdir(data_folder) 
        data.to_csv(os.path.join(data_folder, filename))