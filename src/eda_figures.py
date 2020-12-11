""""
Script for preparing and saving the figures used for the eda analysis of the white wine dataset.

Usage:
    eda_figures.py <data_folder> <raw_data_file> <results_folder>

Options:
"""
from docopt import docopt
import pandas as pd
import altair as alt
import os
import random

def make_eda_figures(data_folder, raw_data_file, results_folder):
    """Function for preparing and saving the figures used for the eda analysis of the white wine dataset

    Parameters:
    data_folder (str): raw data directory
    raw_data_file (str): raw data filename
    results_folder (str): directory to save results in

    Returns:
    
    Example:
    make_eda_figures('data', 'raw_data.csv', 'results')

   """
    random.seed(2020)

    if not type(data_folder) == str:
        raise ValueError("data_folder argument should be passed as str.")
    if not type(raw_data_file) == str:
        raise ValueError("raw_data_file argument should be passed as str.")
    if not type(results_folder) == str:
        raise ValueError("results_folder argument should be passed as str.")

    # Read raw data from download_data.py script
    white_wine_df = pd.read_csv(
        os.path.join(os.path.join(data_folder, raw_data_file)), index_col=0
    )

    # Read preprocessed data from preprocess.py script
    train_df = pd.read_feather(os.path.join(data_folder, "train_df.feather"))
    test_df = pd.read_feather(os.path.join(data_folder, "test_df.feather"))
    X_train = train_df.drop(columns=["quality"])
    y_train = train_df["quality"]
    X_test = test_df.drop(columns=["quality"])
    y_test = test_df["quality"]

    # Make first figure (the distributions for quality)
    y_train_chart = (
        alt.Chart(pd.DataFrame(y_train), title="Train data")
        .mark_bar(size=55)
        .encode(
            x=alt.X("quality", axis=alt.Axis(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            y="count()",
        )
    )
    y_test_chart = (
        alt.Chart(pd.DataFrame(y_test), title="Test data")
        .mark_bar(size=55)
        .encode(
            x=alt.X("quality", axis=alt.Axis(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
            y="count()",
        )
    )
    quality_distributions = y_train_chart | y_test_chart

    # # Make second figure
    # cor_data = (
    #     white_wine_df.corr()
    #     .stack()
    #     .reset_index()
    #     .rename(
    #         columns={0: "correlation", "level_0": "variable", "level_1": "variable2"}
    #     )
    # )
    # cor_data["correlation_label"] = cor_data["correlation"].map(
    #     "{:.2f}".format
    # )  # Round to 2 decimal
    # base = alt.Chart(cor_data).encode(x="variable2:O", y="variable:O")

    # # Text layer with correlation labels
    # # Colors are for easier readability
    # text = base.mark_text().encode(
    #     text="correlation_label",
    #     color=alt.condition(
    #         alt.datum.correlation > 0.5, alt.value("white"), alt.value("black")
    #     ),
    # )

    # # The correlation heatmap itself
    # cor_plot = base.mark_rect().encode(
    #     alt.Color(
    #         "correlation:Q", scale=alt.Scale(domain=(-1, 1), scheme="purpleorange")
    #     )
    # )
    # cor_plot_text = (
    #     (cor_plot + text)
    #     .properties(height=600, width=600)
    #     .configure_axis(labelFontSize=16)
    #     .configure_legend(titleFontSize=15)
    # )

    # Save figures as png
    if not os.path.isdir(results_folder):
        os.mkdir(results_folder)
    quality_distributions.save(
        os.path.join(results_folder, "quality_distributions_figure.png")
    )
    # cor_plot_text.save(os.path.join(results_folder, "corr_figure.png"))


if __name__ == "__main__":
    args = docopt(__doc__)
    make_eda_figures(
        args["<data_folder>"], args["<raw_data_file>"], args["<results_folder>"]
    )

