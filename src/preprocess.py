from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd

def preprocess_data(raw_data_file):
    """Function for preprocessing the white wine quality dataset

    Parameters:
    raw_data_path (str): raw data file

    Returns:
    X_train (pandas.core.frame.DataFrame): training data
    X_test (pandas.core.frame.DataFrame): training data
    y_train (pandas.core.series.Series): training data
    y_test (pandas.core.series.Series): training data
    
    Example:
    X_train, X_test, y_train, y_test = download_data('data/raw_data.csv')

   """
    
    raw_data = pd.read_csv(raw_data_file)
    
    numeric_features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                    'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']

    numeric_transformer = make_pipeline(StandardScaler())

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
        ]
    )
    
    # Keep 25% of data for testing and split data into X and y:
    train_df, test_df = train_test_split(raw_data, test_size=0.25, random_state=123)

    X_train = train_df.drop(columns=['quality'])
    y_train = train_df['quality']
    X_test = test_df.drop(columns=['quality'])
    y_test = test_df['quality']
    
    # Apply the preprocessor to the data
    columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 
               'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    X_train = pd.DataFrame(preprocessor.fit_transform(X_train), columns=columns)
    X_test = pd.DataFrame(preprocessor.transform(X_test), columns=columns)
    return X_train, X_test, y_train, y_test