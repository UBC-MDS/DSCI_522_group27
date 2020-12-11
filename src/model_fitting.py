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
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import altair as alt
import random


def initial_crossval(data_folder, results_folder):
    """Function for preparing and saving the initial cross validation results for several models on the white wine dataset.

    Parameters:
    data_folder (str): raw data directory
    results_folder (str): directory to save results in

    Returns:
    
    Example:
    initial_crossval('data', 'results')

   """
    random.seed(2020)

    if not type(data_folder) == str:
        raise ValueError("data_folder argument should be passed as str.")
    if not type(results_folder) == str:
        raise ValueError("results_folder argument should be passed as str.")

    # Read preprocessed data from data folder
    train_df = pd.read_feather(os.path.join(data_folder, "train_df.feather"))
    test_df = pd.read_feather(os.path.join(data_folder, "test_df.feather"))

    # Split into X and y
    X_train = train_df.drop(columns=["quality"])
    y_train = train_df["quality"]
    X_test = test_df.drop(columns=["quality"])
    y_test = test_df["quality"]

    # Perform intial cross val for several regression models
    results_dict = {}
    models = {
        "dummyregressor": DummyRegressor(),
        "ridge": Ridge(random_state=2020),
        "randomforest": RandomForestRegressor(random_state=2020),
    }

    scoring = {
        "neg_mean_absolute_error": "neg_mean_absolute_error",
        "r2": "r2",
    }

    for model_name, model in models.items():
        pipe = make_pipeline(model)
        scores = cross_validate(
            pipe, X_train, y_train, return_train_score=True, scoring=scoring,
        )
        scores_df = pd.DataFrame(scores).mean()
        results_dict[model_name] = scores_df

    # Save results dataframe as feather
    initial_crossval_results = pd.DataFrame(results_dict)
    initial_crossval_results.reset_index().to_feather(
        os.path.join(results_folder, "initial_crossval_results.feather",),
        compression="uncompressed",
    )


def hyperparameter_tuning(data_folder, results_folder):
    """Function for preparing and saving the tuned model cross validation results for the white wine dataset.

    Parameters:
    data_folder (str): raw data directory
    results_folder (str): directory to save results in

    Returns:
    
    Example:
    hyperparameter_tuning('data', 'results')

   """
    random.seed(2020)

    if not type(data_folder) == str:
        raise ValueError("data_folder argument should be passed as str.")
    if not type(results_folder) == str:
        raise ValueError("results_folder argument should be passed as str.")

    # Make the RandomizedSearchCV object
    pipe_randomforest = make_pipeline(RandomForestRegressor(random_state=2020))
    param_grid = {
        "randomforestregressor__n_estimators": [
            200,
            400,
            600,
            800,
            1000,
            1200,
            1400,
            1600,
            1800,
            2000,
        ],
        "randomforestregressor__max_depth": [
            10,
            20,
            30,
            40,
            50,
            60,
            70,
            80,
            90,
            100,
            None,
        ],
        "randomforestregressor__min_samples_leaf": [1, 2, 4],
        "randomforestregressor__min_samples_split": [2, 5, 10],
    }
    random_search = RandomizedSearchCV(
        pipe_randomforest,
        param_distributions=param_grid,
        n_iter=28,
        cv=3,
        n_jobs=-2,
        random_state=2020,
    )

    # Read preprocessed data from data folder
    train_df = pd.read_feather(os.path.join(data_folder, "train_df.feather"))
    test_df = pd.read_feather(os.path.join(data_folder, "test_df.feather"))

    # Split into X and y
    X_train = train_df.drop(columns=["quality"])
    y_train = train_df["quality"]
    X_test = test_df.drop(columns=["quality"])
    y_test = test_df["quality"]

    # Fit random search to the data and score the resulting best model
    random_search.fit(X_train, y_train)
    print("\nTuned Model Parameters: \n" + str(random_search.best_estimator_))

    results_dict = {}
    scoring = {
        "neg_mean_absolute_error": "neg_mean_absolute_error",
        "r2": "r2",
    }
    scores = cross_validate(
        random_search.best_estimator_,
        X_train,
        y_train,
        return_train_score=True,
        scoring=scoring,
    )
    scores_df = pd.DataFrame(scores).mean()
    results_dict["Tuned Model"] = scores_df
    tuned_crossval_results = pd.DataFrame(results_dict)
    tuned_crossval_results.reset_index().to_feather(
        os.path.join(results_folder, "tuned_crossval_results.feather"),
        compression="uncompressed",
    )

    test_model = random_search.best_estimator_.fit(X_train, y_train)
    y_pred = test_model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    test_results_dict = {}
    test_results_dict["Test Results"] = {
        "neg_mean_absolute_error": -1 * mae,
        "r2": r2,
    }

    test_results_df = pd.DataFrame(test_results_dict)
    test_results_df.reset_index().to_feather(
        os.path.join(results_folder, "tuned_test_results.feather"),
        compression="uncompressed",
    )

    # Make feature importance figure:
    importance = random_search.best_estimator_.named_steps[
        "randomforestregressor"
    ].feature_importances_
    weights_df = pd.DataFrame(
        {"target_feats": X_train.columns, "target_weights": importance.transpose()}
    )
    weigths_figure = (
        alt.Chart(weights_df)
        .mark_bar()
        .encode(
            x=alt.X("target_feats", sort="-y", title="target features"),
            y=alt.Y("target_weights", title="target weights"),
        )
        .properties(width=400, height=400)
        .configure_axis(labelFontSize=16)
    )
    weigths_figure.save(os.path.join(results_folder, "weights_figure.png"))

    # We noticed some of the weights were much higher than others...
    # What if we run a model with only the highest weight features?
    X_train_reduced = X_train.drop(
        columns=[
            "pH",
            "total sulfur dioxide",
            "residual sugar",
            "chlorides",
            "sulphates",
            "fixed acidity",
            "density",
            "citric acid",
        ]
    )
    X_test_reduced = X_test.drop(
        columns=[
            "pH",
            "total sulfur dioxide",
            "residual sugar",
            "chlorides",
            "sulphates",
            "fixed acidity",
            "density",
            "citric acid",
        ]
    )
    # Need to perform a second round of hyperparameter tuning
    random_search_reduced = RandomizedSearchCV(
        pipe_randomforest,
        param_distributions=param_grid,
        n_iter=28,
        cv=3,
        n_jobs=-2,
        random_state=2020,
    )

    results_dict = {}
    random_search_reduced.fit(X_train_reduced, y_train)
    print(
        "\nTuned Model Parameters (Reduced Features): \n"
        + str(random_search.best_estimator_)
    )

    scores = cross_validate(
        random_search_reduced.best_estimator_,
        X_train_reduced,
        y_train,
        return_train_score=True,
        scoring=scoring,
    )
    reduced_model_scores_df = pd.DataFrame(scores).mean()
    results_dict["Tuned Model (Reduced Features)"] = reduced_model_scores_df

    reduced_tuned_crossval_results = pd.DataFrame(results_dict)
    reduced_tuned_crossval_results.reset_index().to_feather(
        os.path.join(results_folder, "reduced_tuned_crossval_results.feather"),
        compression="uncompressed",
    )

    reduced_test_model = random_search_reduced.best_estimator_.fit(
        X_train_reduced, y_train
    )
    y_pred_reduced = reduced_test_model.predict(X_test_reduced)
    mae = mean_absolute_error(y_test, y_pred_reduced)
    r2 = r2_score(y_test, y_pred_reduced)

    test_results_dict = {}
    test_results_dict["Test Results"] = {
        "neg_mean_absolute_error": -1 * mae,
        "r2": r2,
    }

    test_results_df = pd.DataFrame(test_results_dict)
    test_results_df.reset_index().to_feather(
        os.path.join(results_folder, "reduced_tuned_test_results.feather"),
        compression="uncompressed",
    )


if __name__ == "__main__":
    args = docopt(__doc__)
    initial_crossval(args["<data_folder>"], args["<results_folder>"])
    hyperparameter_tuning(args["<data_folder>"], args["<results_folder>"])

