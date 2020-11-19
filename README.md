# Predicting white wine quality

  - author: DSCI_522_group27

A group project for DSCI 522 in MDS program in UBC.

# Proposal 

We will work with the wine quality data set created by Dr. P. Cortez, 
A. Cerdeira, F. Almeida, T. Matos and J. Reis. It was sourced from the UCI Machine Learning Repository, 
and you can find it [here](https://archive.ics.uci.edu/ml/datasets/wine+quality). 
This data set has two primary data: white wine data and red wine data. 
We will work on the white wine data since this data has many more observations by comparing the red wine data observations. 
However, we may use red wine data by comparing the white wine data to do more complex investigations. 

In this data set, we are interested in predicting the wine quality based on physicochemical tests. 
We will focus on predicting the white wine quality based on physicochemical tests,
a regression problem, by treating quality as our target since the quality is numeric scores with a range from 0 to 10.
There are 11 features (numeric variables): a set of physicochemical test results such as citric acid, free sulfur dioxide, 
density and so on in both the white wine data and the red wine data. Each row has this set of physicochemical test results, 
and we have 4898 observations in total with no missing values in the white wine data. 
Please note that these quality scores in this white wine data are based on sensory data.

The plan for analyzing the white wine data is to use a scikit-learn regression model to 
predict the wine quality based on physicochemical tests. We will use different regression models 
such as the linear regression model (`Ridge` or `LinearRegression`), random forest trees to get a correct and accurate prediction. 

Looking through the white wine data, we have a set of physicochemical tests such as pH,
free sulfur dioxide, etc. We want to know if our features are correlated or not. 
If our features are related, we need to use `Ridge` instead of `LinearRegression` to avoid a bad predicting issue. 
Then we can visualize correlation plots by doing exploratory data analysis. 
We can get a summary report by using Pandas profiling to do exploratory data analysis on data. 

If we have several analysis results, we will create a result folder at the root of our group repository 
and add our tables and figures into this result folder.


# License 
The materials on predicting white wine quality are licensed under the MIT License 
(Copyright (c) 2020 Master of Data Science at the University of British Columbia)

# References

P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.