import pandas as pd
import os
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
cwd = os.getcwd()
data.to_csv(os.path.join(cwd, 'white_wine_quality.csv'))
