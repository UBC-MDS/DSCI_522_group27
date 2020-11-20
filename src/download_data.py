""""
Usage:
    download_data.py <data_folder> <filename>

Options:

"""
from docopt import docopt
import pandas as pd
import os

if __name__ == "__main__":
    
    args = docopt(__doc__)
    
    import pandas as pd
    import os
    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
    cwd = os.getcwd()
    data_folder = os.path.join(cwd, args['<data_folder>'])
    data.to_csv(os.path.join(data_folder, args['<filename>']))

# To use this script with jupyter notebooks to download data into /data folder call: !python download_data.py data raw.csv

def download_data(database_name,filename):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/'
    url = os.path.join(url,database_name)
    url = os.path.join(url,filename)
    data = pd.read_csv(url, sep=';')
    return data