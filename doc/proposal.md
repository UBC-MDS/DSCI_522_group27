# Predicting white wine quality

  - author: DSCI 522 group 27

This is a group project for DSCI 522 in the MDS program at UBC.

# Proposal 

For this project, we are interested in predicting subjective wine quality scores, as scored by wine reviewers, based on a set of physicochemical features of the wine.

We will work with the wine quality data set created by Dr. P. Cortez, 
Dr. A. Cerdeira, Dr. F. Almeida, Dr. T. Matos and Dr. J. Reis. It was sourced from the UCI Machine Learning Repository (Cortez et al., 2009), 
and you can find it [here](https://archive.ics.uci.edu/ml/datasets/wine+quality). 
This dataset has two primary groups: white wine data and red wine data. 
We have chosen to analyse the white wine data since this data has many more observations than the red wine data observations. 
However, we may also add the red wine data into our analysis if time allows. 

We aim to predict the quality of different wines based on their physicochemical features which are included in the dataset. We will be treaing this as a regression problem in Machine learning, by using quality as our target (quality is numeric with scores from 3 to 9, assumed to be given on a 1-10 rating scale).
There are 11 numeric features in the dataset, which includes physicochemical test results such as citric acid content, free sulfur dioxide content, density, etc. for both the white wine and the red wine data. Each row contains one observation of these physicochemical test results and the resulting quality, and we have 4898 observations in total with no missing values in the white wine data. Note that the quality scores in this white wine data are based on sensory data and are score subjectively by reviewers.

The plan for analyzing the white wine data involves using a scikit-learn regression model to predict the wine quality based on the physicochemical test features.
We will test different regression models 
such as the linear regression model (`Ridge` or `LinearRegression`) and the random forest trees model to try and train an accurate prediction model for white wine quality. 

One of the first steps of this project will be to perform and exploratory data analysis on the white wine dataset. Looking through the white wine data, we have a set of physicochemical tests such as pH,
free sulfur dioxide, etc. and we want to know if our features are correlated or not. 
If our features are related, we need to use `Ridge` instead of `LinearRegression` to avoid low prediction scores. 
We then visualized correlation plots to observe which features were strongly correlated to each other, and also plotted histograms to uncover how features were correlated to the quality targets. A pandas profiling report was also produced to check feature distributions, check for missing values, and other general eda for our data.

The completed EDA analysis can be found in the eda folder at the root of our group's repository.

## Usage

To replicate the analysis, clone this GitHub repository, install the dependencies listed below, and run the following commands from the main directory of the project:
- python src/download_data.py data raw_data.csv
- python src/preprocess.py data raw_data.csv
- python src/eda_figures.py data raw_data.csv results

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
