# Predicting white wine quality

  - author: DSCI 522 group 27

This is a group project for DSCI 522 in the MDS program at UBC.

## About

Here we attempt to build a regression model which can use physicochemical features of a wine to accurately predict the quality rating of the wine, as it would have been rated by a reviewer. Running the ridge and random forest regressor models through cross-validation, we found the later to deliver a much higher training score. However, as there was a clear case of overfitting, we ran hyperparameter optimization in an attempt to improve the model. Unfortunately, the test score with the best hyperparameters was only around 0.505 (Note that we have imbalanced data). Using the feature importances attribute in random forest regressor, we were able to obtain feature coefficients that confirmed that the alcohol feature had the highest coeffiecient score, this was also our expectation from our initial EDA. In the coming weeks, we intend to refine the model further and/or try other models that may adopt better to our dataset and deliver a higher test score.

The dataset that was used for this project is of physicochemical features of wines with the corresponding wine quality ratings, this data set was created by Dr. P. Cortez, Dr. A. Cerdeira, Dr. F. Almeida, Dr. T. Matos and Dr. J. Reis. It was sourced from the UCI Machine Learning Repository (Cortez et al., 2009), and you can find it [here](https://archive.ics.uci.edu/ml/datasets/wine+quality). This dataset has two primary groups: white wine data and red wine data. We have chosen to analyse the white wine data since this data has many more observations than the red wine data observations. Note that the quality scores in this wine dataset are based on sensory data and are scored subjectively by reviewers.

## Report

The final report can be found [here](https://htmlpreview.github.io/?https://github.com/UBC-MDS/DSCI_522_group27/blob/main/doc/white_wine_predict_report.html)

## Usage

To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands from the main directory of the project:
```
# download data and save as csv
python src/download_data.py data raw_data.csv

# preprocess and split data
python src/preprocess.py data raw_data.csv

# create exploratory data analysis figures
python src/eda_figures.py data raw_data.csv results

# fit, tune and test model
python src/model_fitting.py data results

# render final report
Rscript -e "rmarkdown::render('doc/white_wine_predict_report.Rmd', output_format = 'github_document')"
```
## Dependencies

  - Python 3.7 and Python packages:
      - docopt==0.6.2
      - pandas==0.24.2
      - pandas-profiling==2.9.0
      - matplotlib==3.3.3
      - altair==4.1.0
      - numpy==1.19.4
      - sklearn==0.23.2
 
# License 
The materials on predicting white wine quality are licensed under the MIT License 
(Copyright (c) 2020 Master of Data Science at the University of British Columbia)

# References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.
