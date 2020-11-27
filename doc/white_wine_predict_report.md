---
title: "white_wine_predict_report"
author: "DSCI 522 group 27"
bibliography: references.bib
output: 
  html_document:
    toc: true
    keep_md: true
---



# Predicting quality of white wine from various characteristics

# **Summary**

Here we tried different models such as `DummyRegressor`, `Ridge` and `RandomForestRegressor` to predict the white wine quality. When we carried out the cross-validation for these three models, we chose `RandomForestRegressor` as our best performance model by comparing different metrics. We tried hyperparameter optimization with `RandomForestRegressor` to get the final test score around 0.4311, which seems to be not reasonable here. Therefore, `RandomForestregressor` may not be an appropriate model to use here. However, we can find other models to improve our test scores, or we can carry out a different metric or tune other hyperparameters to get a better result.

# **Introduction**

The wine market occupies a significant position among consumers. For manufacturers, the quality of alcohol significantly affects the sales of alcoholic beverages, but the taster is not necessarily the only standard for judging the quality of alcoholic beverages. We can establish a model to estimate the quality of alcoholic drinks through chemical substances. However, this may require a lot of professional knowledge. We found a good article which was written by Dr. P. Cortez, Dr. A. Cerdeira, Dr. F. Almeida, Dr. T. Matos and Dr. J. Reis, and they used a data mining approach to get promising results comparing neural network methods [@CORTEZ2009547].

Here we want to try different regression models to predict the wine quality based on the physicochemical test features. Answering this question is crucial since we want to support the wine tasting evaluations of oenologists and contribute to wine production [@CORTEZ2009547].

# **Methods**

## **Data**

The dataset that we used came from the University of California Irvine (UCI) machine learning repository and was collected by Paulo Cortez, University of Minho, Guimarães, Portugal and A. Cerdeira, F. Almeida, T. Matos with help from J. Reis, Viticulture Commission of the Vinho Verde Region(CVRVV), Porto, Portugal in 2009. The dataset contains the results of various physiochemical tests on white "Vinho Verde" wine samples from Northern Portugal and can be found [here](https://archive.ics.uci.edu/ml/datasets/wine+quality) specifically with the [white wine dataset](%5Bhttps://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv).](<https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv>).) No additional features or specific branding of each wine is available in the dataset for privacy purposes. Each row in the dataset represents a single wine which was tested and scored based on sensory data.

## **Analysis**

A classification model was built with [@Python] scripts using the [@scikit-learn] `RandomForestRegressor` algorithm was and allowed us to predict a sensory score based on the physiochemical testing information recorded for each wine. Because of the privacy constraints of the data our dataset is somewhat limited since useful potentially factors that might influence the scoring such as grape types, brand names, or price are not available to us. Assumptions we made regarding this dataset are that the quality scores came from the opinions of wine critics and that testing for all wines was consistent. The model was fit using all??? of the variables from the dataset. Hyperparameters `n_estimators` and `max_depth` were optimized via random search while all other hyperparameters used the default sklearn `RandomForestRegressor` values. Some potential limitations of this model are that \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_. If provided with more time we would be able to improve our analysis by \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_. The data was processed using the [@reback2020pandas] package. This document was compiled using an [@R] document file with scripts run using the [@docopt] package.

# **Results & Discussion**

To determine how useful strong of an influence each feature has on the quality score we created a correlation plot using the altair package which shows how each of the different features is correlated with each other. This chart showed us that different features had varying degrees of influence on the quality score, with increased alcohol content and decreased density most heavily influencing the quality score.

 

<div class="figure">
<img src="../results/feature_correlation.png" alt="Altair correlation plot of the correlation of each of the different features in the white wine dataset." width="60%" />
<p class="caption">Altair correlation plot of the correlation of each of the different features in the white wine dataset.</p>
</div>

 

We found that a random forest classifier with hyperparaters `n_estimators` and `max_depth` set to values of 300 and 10 respectively worked best with our dataset. This resulted in use producing a model with a training score of 0.929264 and a testing score of 0.499623.

 

<div class="figure">
<img src="../results/feature_weight.png" alt="Figure 2. ______" width="60%" />
<p class="caption">Figure 2. ______</p>
</div>

STILL NEED TO FIND REFERENCES FOR...

-   docopt (maybe need python version)?

-   os

# References
