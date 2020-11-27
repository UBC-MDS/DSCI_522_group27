""""
Script for building and fitting machine learning models to the white wine dataset.

Usage:
    model_fitting.py <data_folder> <results_folder>

Options:
"""
from docopt import docopt
import pandas as pd
import os
from sklearn.model_selection import cross_val_score, cross_validate, RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.compose import ColumnTransformer
import altair as alt

def initial_crossval(data_folder, results_folder):
    """Function for preparing and saving the initial cross validation results for several models on the white wine dataset.

    Parameters:
    data_folder (str): raw data directory
    results_folder (str): directory to save results in

    Returns:
    
    Example:
    initial_crossval('data', 'results')

   """
    # Read preprocessed data from data folder
    train_df = pd.read_feather(os.path.join(data_folder, 'train_df.feather'))
    test_df = pd.read_feather(os.path.join(data_folder, 'test_df.feather'))
    
    # Split into X and y
    X_train = train_df.drop(columns=['quality'])
    y_train = train_df['quality']
    X_test = test_df.drop(columns=['quality'])
    y_test = test_df['quality']
    
    # Perform intial cross val for several regression models
    results_dict = {}
    models = {
        "dummyregressor": DummyRegressor(),
        "ridge": Ridge(),
        "randomforest": RandomForestRegressor(),
    }

    scoring={
            "neg_mean_squared_error": "neg_mean_squared_error",
            "neg_root_mean_square": "neg_root_mean_squared_error",
            "neg_mean_absolute_error": "neg_mean_absolute_error",
            "r2": "r2"
         }

    for model_name, model in models.items():
        pipe = make_pipeline(model)
        scores = cross_validate(pipe, X_train, y_train, return_train_score= True, scoring = scoring)
        scores_df = pd.DataFrame(scores).mean()
        results_dict[model_name] = scores_df
    
    # Save results dataframe as feather
    initial_crossval_results = pd.DataFrame(results_dict)
    initial_crossval_results.reset_index().to_feather(os.path.join(results_folder, 'initial_crossval_results.feather'))
    
def hyperparameter_tuning(data_folder, results_folder):
    """Function for preparing and saving the tuned model cross validation results for the white wine dataset.

    Parameters:
    data_folder (str): raw data directory
    results_folder (str): directory to save results in

    Returns:
    
    Example:
    hyperparameter_tuning('data', 'results')

   """
    # Make the RandomizedSearchCV object
    pipe_randomforest = make_pipeline(RandomForestRegressor())
    param_grid = {
        "randomforestregressor__n_estimators": [300, 600, 900],
        "randomforestregressor__max_depth": [10, 20, 30, 40],
        "randomforestregressor__bootstrap": [True, False],
        "randomforestregressor__min_samples_leaf": [1, 2, 4],
        "randomforestregressor__min_samples_split": [2, 5, 10]
    }
    random_search = RandomizedSearchCV(
        pipe_randomforest, 
        param_distributions=param_grid,
        n_iter=28,
        cv=3,
        n_jobs=-1,
        random_state=2020
    )
    
    # Read preprocessed data from data folder
    train_df = pd.read_feather(os.path.join(data_folder, 'train_df.feather'))
    test_df = pd.read_feather(os.path.join(data_folder, 'test_df.feather'))
    
    # Split into X and y
    X_train = train_df.drop(columns=['quality'])
    y_train = train_df['quality']
    X_test = test_df.drop(columns=['quality'])
    y_test = test_df['quality']
    
    # Fit random search to the data and score the resulting best model
    random_search.fit(X_train, y_train)
    
    results_dict = {}
    scoring={
        "neg_mean_squared_error": "neg_mean_squared_error",
        "neg_root_mean_square": "neg_root_mean_squared_error",
        "neg_mean_absolute_error": "neg_mean_absolute_error",
        "r2": "r2"
     }
    scores = cross_validate(random_search.best_estimator_, X_train, y_train, return_train_score= True, scoring = scoring)
    scores_df = pd.DataFrame(scores).mean()
    results_dict['Tuned Model'] = scores_df
    tuned_crossval_results = pd.DataFrame(results_dict)
    tuned_crossval_results.reset_index().to_feather(os.path.join(results_folder, 'tuned_crossval_results.feather'))
    
    print("Random Search best model r2 score: " + str(random_search.best_score_))
    print("Train r2 score: " + str(random_search.score(X_train, y_train)))
    print("Test r2 score: " + str(random_search.score(X_test, y_test)))
    
    # Make feature importance figure:
    importance = random_search.best_estimator_.named_steps["randomforestregressor"].feature_importances_
    weights_df = pd.DataFrame(
    {
        "target_feats": X_train.columns,
        "target_weights": importance.transpose()
    })
    weigths_figure = alt.Chart(weights_df).mark_bar().encode(x = alt.X("target_feats", sort = '-y', title = "target features"),
                                y = alt.Y("target_weights", title = "target weights")
                               ).properties(width = 400, height = 400
                                           ).configure_axis(labelFontSize = 16
    )
    weigths_figure.save(os.path.join(results_folder, 'weigths_figure.html'))


    
    
if __name__ == "__main__":
    args = docopt(__doc__)
    initial_crossval(args['<data_folder>'], args['<results_folder>'])
    hyperparameter_tuning(args['<data_folder>'], args['<results_folder>'])