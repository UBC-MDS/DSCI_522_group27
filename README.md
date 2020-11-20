# Predicting white wine quality

  - author: DSCI 522 group 27

This is a group project for DSCI 522 in the MDS program at UBC.

# Proposal 

For this project, we are interested in studying the relationship between the chemical contents of different wines and their subjective qualities as scored by wine reviewers.

We will work with the wine quality data set created by Dr. P. Cortez, 
A. Cerdeira, F. Almeida, T. Matos and J. Reis. It was sourced from the UCI Machine Learning Repository, 
and you can find it [here](https://archive.ics.uci.edu/ml/datasets/wine+quality). 
This dataset has two primary groups: white wine data and red wine data. 
We have chosen to analyse the white wine data since this data has many more observations than the red wine data observations. 
However, we may also add the red wine data into our analysis if time allows. 

We aim to predict the quality of diffrent wines based on their physicochemical features which are included in the dataset,
a regression problem in Machine learning, by treating quality as our target (quality is numeric with scores from 0 to 10).
There are 11 numeric features in the dataset, which includes physicochemical test results such as citric acid content, free sulfur dioxide content, 
density, etc. for both the white wine and the red wine data. Each row contains one observation of these physicochemical test results and the resulting quality,
and we have 4898 observations in total with no missing values in the white wine data. 
Please note that these quality scores in this white wine data are based on sensory data and are score subjectively by reviewers.

The plan for analyzing the white wine data involves using a scikit-learn regression model to predict the wine quality based on the physicochemical test features.
We will test different regression models 
such as the linear regression model (`Ridge` or `LinearRegression`) and the random forest trees model to try and train an accurate prediction model for white wine quality. 

One of the first steps of this project will be to perform and exploratory data analysis on the white wine dataset. Looking through the white wine data, we have a set of physicochemical tests such as pH,
free sulfur dioxide, etc. and we want to know if our features are correlated or not. 
If our features are related, we need to use `Ridge` instead of `LinearRegression` to avoid a bad predicting issue. 
Then we can visualize correlation plots and calculating correlations to form a correlation table to do exploratory data analysis. 
We can get a summary report by using Pandas profiling to do exploratory data analysis on data. 

We can create an eda folder at the root of our group repository 
and add our tables and figures into this eda folder.

# License 
The materials on predicting white wine quality are licensed under the MIT License 
(Copyright (c) 2020 Master of Data Science at the University of British Columbia)

# References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.
