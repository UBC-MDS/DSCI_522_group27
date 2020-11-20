# Predicting white wine quality

  - author: DSCI 522 group 27

This is a group project for DSCI 522 in the MDS program at UBC.

# Proposal 

For this project, we will work with the wine quality data set created by Dr. P. Cortez, 
A. Cerdeira, F. Almeida, T. Matos and J. Reis. It was sourced from the UCI Machine Learning Repository, 
and you can find it [here](https://archive.ics.uci.edu/ml/datasets/wine+quality). 
This data set has two primary data: white wine data and red wine data. 
For this project we will work primarily with the white wine data since this data has many more observations.

In this data set, we are interested in predicting the wine quality based on physicochemical tests. The question we are trying to anwer is: given a set of physicochemical properties, what is the predicted quality rating of the wine? 
We will be treating this as a regression problem in Machine learning, with quality serving as our target. Quality is numeric with scores from 3 to 9 (assumed to be scored on a 1-10 rating scale).
The data set consists of  11 features (numeric variables): a set of physicochemical tests such as citric acid, free sulfur dioxide, density, etc. Each row has this set of physicochemical tests, there are 4898 observations in total with no missing values in the white wine data. Note that these quality scores in this white wine data are based on sensory data.

The plan for analyzing the white wine data uses a scikit-learn regression model to predict the wine quality based on physicochemical tests. We will use different regression models such as the linear regression model (`Ridge` or `LinearRegression`), random forest trees to get a correct and accurate prediction. 

Looking through the white wine data, we have a set of physicochemical tests such as pH,free sulfur dioxide, etc. We want to know if our features are correlated or not. If our features are related, we need to use `Ridge` instead of `LinearRegression` to avoid a bad predicting issue. Then we can visualize correlation plots and calculating correlations to form a correlation table to do exploratory data analysis. We can get a summary report by using Pandas profiling to do exploratory data analysis on data. We can create an eda folder at the root of our group repository and add our tables and figures into this eda folder.


# License 
The materials on predicting white wine quality are licensed under the MIT License 
(Copyright (c) 2020 Master of Data Science at the University of British Columbia)

# References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.