""""
Script for preprocessing and train-test splitting the white wine dataset.

Usage:
    preprocess.py <data_folder> <raw_data_file>

Options:
"""
from docopt import docopt
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd
import os
import random

def preprocess_data(data_folder, raw_data_file):
    """Function for preprocessing the white wine quality dataset

    Parameters:
    data_folder   (str): data directory
    raw_data_file (str): raw data file

    Returns:
    train_df (pandas.core.frame.DataFrame): training data
    test_df  (pandas.core.frame.DataFrame): training data
    
    Example:
    train_df, test_df = preprocess_data('data', 'raw_data.csv')

   """
    random.seed(2020)
    if not type(data_folder) == str:
        raise ValueError("data_folder argument should be passed as str.")
    if not type(raw_data_file) == str:
        raise ValueError("raw_data_file argument should be passed as str.")

    # Read raw data from data folder:
    raw_data = pd.read_csv(os.path.join(data_folder, raw_data_file), index_col=0)
    numeric_features = [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol",
    ]

    # Set up preprocessing pipeline:
    numeric_transformer = make_pipeline(StandardScaler())
    preprocessor = ColumnTransformer(
        transformers=[("num", numeric_transformer, numeric_features),],
        remainder="passthrough",
    )  # quality should passthrough pipeline since it is the target

    # Keep 25% of data for testing and split data into X and y:
    train_df, test_df = train_test_split(raw_data, test_size=0.25, random_state=123)

    # Apply the preprocessor to the data:
    columns = [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol",
        "quality",
    ]
    train_df = pd.DataFrame(preprocessor.fit_transform(train_df), columns=columns)
    test_df = pd.DataFrame(preprocessor.transform(test_df), columns=columns)
    return train_df, test_df


if __name__ == "__main__":
    args = docopt(__doc__)
    train_df, test_df = preprocess_data(args["<data_folder>"], args["<raw_data_file>"])

    train_df.to_feather(
        os.path.join(args["<data_folder>"], "train_df.feather"),
        compression="uncompressed",
    )
    test_df.to_feather(
        os.path.join(args["<data_folder>"], "test_df.feather"),
        compression="uncompressed",
    )

