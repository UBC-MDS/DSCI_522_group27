Predicting quality of white wine from various characteristics
================
DSCI 522 group 27

# **Summary**

Here we tried different models such as dummy regressor, ridge and random
forest regressor to predict the white wine quality. When we carried out
the cross-validation for these three models, we chose random forest
regressor as our best performance model by comparing different metrics.
We tried hyperparameter optimization with random forest regressor to get
the r2 score of 0.492 as our final test score with a negative mean
absolute error of -0.443, which seems to be not reasonable here (Note
that we have imbalanced data). Therefore, random forest regressor may
not be an appropriate model to use here. However, we can find other
complex models to improve our test scores, or we can carry out a
different metric or tune other hyperparameters to get a better result.
Moreover, we can also change the prediction task from a regression
problem to a classification problem in order to find a better
prediction.

# **Introduction**

The wine market occupies a significant position among consumers. For
manufacturers, the quality of alcohol significantly affects the sales of
alcoholic beverages, but the taster is not necessarily the only standard
for judging the quality of alcoholic beverages. We can establish a model
to estimate the quality of alcoholic drinks through chemical substances.
However, this may require a lot of professional knowledge. We found a
good article which was written by Dr. P. Cortez, Dr. A. Cerdeira, Dr. F.
Almeida, Dr. T. Matos and Dr. J. Reis, and they used a data mining
approach to get promising results comparing neural network methods
(Cortez et al. 2009).

Here we want to try different regression models to predict the wine
quality based on the physicochemical test features. Answering this
question is crucial since we want to support the wine tasting
evaluations of oenologists and contribute to wine production (Cortez et
al. 2009).

# **Methods**

## **Data**

The dataset that we used came from the University of California Irvine
(UCI) machine learning repository and was collected by Paulo Cortez,
University of Minho, Guimarães, Portugal and A. Cerdeira, F. Almeida, T.
Matos with help from J. Reis, Viticulture Commission of the Vinho Verde
Region(CVRVV), Porto, Portugal in 2009. The dataset contains the results
of various physiochemical tests on white “Vinho Verde” wine samples from
Northern Portugal and can be found
[here](https://archive.ics.uci.edu/ml/datasets/wine+quality)
specifically with the [white wine
dataset](%5Bhttps://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv).
No additional features or specific branding of each wine is available in
the dataset for privacy purposes. Each row in the dataset represents a
single wine which was tested and scored based on sensory data.

## **Analysis**

A classification model was built with python scripts using the sk-learn
`RandomForestRegressor` algorithm and allowed us to predict a sensory
score based on the physiochemical testing information recorded for each
wine(Van Rossum and Drake 2009), (Pedregosa et al. 2011). Because of the
privacy constraints of the data our dataset is somewhat limited since
useful potentially factors that might influence the scoring such as
grape types, brand names, or price are not available to us. Assumptions
we made regarding this dataset are that the quality scores came from the
opinions of wine critics and that testing for all wines was consistent.
The model was fit using all of the variables from the dataset.
Hyperparameters `n_estimators` and `max_depth` were optimized via random
search while all other hyperparameters used the default sklearn
`RandomForestRegressor` values. The data was processed using the pandas
package and EDA was performed using the pandas-profiling package (team
2020) (Brugman 2019). This document was compiled using an R document
file with scripts run using the docopt package (R Core Team 2019), (de
Jonge 2020). Tables were stored using feather files (with dependency on
arrow) and displayed using knitr’s kable function (Wickham 2019),
(François et al. 2020), (Xie 2020). This document was compiled using
rmarkdown (Allaire et al. 2020).

# **Results & Discussion**

After splitting our dataset into a training set and a validation set we
plotted the distribution of the quality scores for each wine (Figure 1).
Despite the quality scoring being performed a scale from 1-10 only
values in the range of 3-9 were observed. 6 was the most common score
observed across all testing.

<div class="figure">

<img src="../results/quality_distributions_figure.png" alt="Figure 1. Quality distribution of wines in the training and test datasets." width="60%" />
<p class="caption">
Figure 1. Quality distribution of wines in the training and test
datasets.
</p>

</div>

In order to determine which model works best with our data we decided to
test both the `RidgeCV` and `RandomForestRegressor` to compare them
against the dummy regressor model. We present the cross-validation
values of this testing in Table 1. We determined that random forest
methods provided the best training and validation model scores and
decided to proceed with those.

| index                             | dummyregressor |      ridge | randomforest |
|:----------------------------------|---------------:|-----------:|-------------:|
| fit\_time                         |      0.0009194 |  0.0029257 |    1.2327879 |
| score\_time                       |      0.0007301 |  0.0022437 |    0.0190658 |
| test\_neg\_mean\_squared\_error   |     -0.7899251 | -0.5794524 |   -0.3924718 |
| train\_neg\_mean\_squared\_error  |     -0.7896847 | -0.5687437 |   -0.0553803 |
| test\_neg\_mean\_absolute\_error  |     -0.6766545 | -0.5909963 |   -0.4585544 |
| train\_neg\_mean\_absolute\_error |     -0.6765906 | -0.5871736 |   -0.1705949 |
| test\_r2                          |     -0.0007601 |  0.2655188 |    0.5029517 |
| train\_r2                         |      0.0000000 |  0.2797630 |    0.9298684 |

Table 1. Table of cross-validation results for each tested model

We found that a random forest classifier worked best with our dataset
and decided perform random search hyperparameter optimization to tune
the hyperparameters `n_estimators` and `max_depth`, which we determined
produced the best scoring model with the values of 300 and 10
respectively. Running a `RandomForestRegressor` with these
hyperparameters resulted in a training r2 score of 0.929 and a
validation r2 score of 0.505 (Table 2).

| index                             | Tuned Model |
|:----------------------------------|------------:|
| fit\_time                         |   7.1197869 |
| score\_time                       |   0.0974426 |
| test\_neg\_mean\_squared\_error   |  -0.3905119 |
| train\_neg\_mean\_squared\_error  |  -0.0558802 |
| test\_neg\_mean\_absolute\_error  |  -0.4569208 |
| train\_neg\_mean\_absolute\_error |  -0.1736196 |
| test\_r2                          |   0.5053642 |
| train\_r2                         |   0.9292326 |

Table 2. Table of cross-validation results of the tuned random forest
model

Running our hyperparamter tuned `RandomForestClassifier` model on our
test data resulted in an r2 test score of 0.492 and a negative mean
absolute error of -0.443 (Table 3). These results are comparable to
those that we observed in our validation scoring, which produced similar
values (with scoring differing by only about 0.01).

| index                      | Test Results |
|:---------------------------|-------------:|
| neg\_mean\_absolute\_error |   -0.4434123 |
| neg\_mean\_squared\_error  |   -0.3896619 |
| r2                         |    0.4924049 |

Table 3. Tuned test results of RandomForestClassifier.

We then examined the weight of the features present in our best scoring
`RandomForestClassifier` and charted the weight of each in the model
(Figure 2). Alcohol was found to be the feature most heavily associated
with higher wine quality scores with a target weight of 0.24. Other
features such as density, citric acid, and sulphates appear to have
limited weight in our model. In an attempt to further improve the
scoring of our model we decided to cut all features with a target weight
lower than 0.10, meaning we decided to run a model that predicted
quality scores based on the features alcohol, free sulfur dioxide, and
volatile acidity.

<div class="figure">

<img src="../results/weights_figure.png" alt="Figure 2. Bar chart showing the target weights of different features of our RandomForestRegressor model." width="60%" />
<p class="caption">
Figure 2. Bar chart showing the target weights of different features of
our RandomForestRegressor model.
</p>

</div>

# Limitations & Future

Some potential limitations of our model are that we have only tested a
handful of different regression methods and only have performed light
hyperparameter optimization via a random search. There likely exists
combinations of models and hyperparamters (perhaps determined through a
grid search, though this would increase the runtime of our model
significantly) which would lead to better scoring in our model. For
example, using support vector machine (SVM) methods might be a more
effective way to predict wine scores as they were specifically mentioned
by Cortez et al. in their paper analyzing the dataset (Cortez et al.
2009). Another way to improve our model would be to implement a form of
feature selection (such as RFECV) given that we our current method
involves us manually selecting our features based on their target
weights. Another way to improve this model would be to work with a
larger dataset (i.e. with wine/judges from around the world) or with a
greater number of features since the one we are currently working with
does not list some information that could potentially be correlated with
scoring (type of grape used in the wine, price, etc.) which are
currently omitted for the sake of privacy protection.

# References

<div id="refs" class="references hanging-indent">

<div id="ref-rmarkdown">

Allaire, JJ, Yihui Xie, Jonathan McPherson, Javier Luraschi, Kevin
Ushey, Aron Atkins, Hadley Wickham, Joe Cheng, Winston Chang, and
Richard Iannone. 2020. *Rmarkdown: Dynamic Documents for R*.
<https://github.com/rstudio/rmarkdown>.

</div>

<div id="ref-pandasprofiling2019">

Brugman, Simon. 2019. “pandas-profiling: Exploratory Data Analysis for
Python.” <https://github.com/pandas-profiling/pandas-profiling>.

</div>

<div id="ref-CORTEZ2009547">

Cortez, Paulo, Antonio Cerdeira, Fernando Almeida, Telmo Matos, and Jose
Reis. 2009. “Modeling Wine Preferences by Data Mining from
Physicochemical Properties.” *Decision Support Systems* 47 (4): 547–53.
<https://doi.org/https://doi.org/10.1016/j.dss.2009.05.016>.

</div>

<div id="ref-docopt">

de Jonge, Edwin. 2020. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-arrow">

François, Romain, Jeroen Ooms, Neal Richardson, and Apache Arrow. 2020.
*Arrow: Integration to ’Apache’ ’Arrow’*.
<https://CRAN.R-project.org/package=arrow>.

</div>

<div id="ref-scikit-learn">

Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O.
Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in
Python.” *Journal of Machine Learning Research* 12: 2825–30.

</div>

<div id="ref-R">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-reback2020pandas">

team, The pandas development. 2020. *Pandas-Dev/Pandas: Pandas* (version
latest). Zenodo. <https://doi.org/10.5281/zenodo.3509134>.

</div>

<div id="ref-Python">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-feather">

Wickham, Hadley. 2019. *Feather: R Bindings to the Feather ’Api’*.
<https://CRAN.R-project.org/package=feather>.

</div>

<div id="ref-knitr">

Xie, Yihui. 2020. *Knitr: A General-Purpose Package for Dynamic Report
Generation in R*. <https://yihui.org/knitr/>.

</div>

</div>
