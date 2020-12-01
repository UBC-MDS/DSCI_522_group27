# white wine prediciton data pipeline
# author: DSCI 522 group 27
# date: 2020-12-05


all: results/corr_figure.png results/quality_distributions_figure.png results/weights_figure.png results/initial_crossval_results.feather results/tuned_crossval_results.feather doc/white_wine_predict_report.md doc/white_wine_predict_report.html
  
# download data and save as csv
data/raw_data.csv: src/download_data.py
	python src/download_data.py data raw_data.csv

# preprocess and split data
data/test_df.feather data/train_df.feather: src/preprocess.py data/raw_data.csv
	python src/preprocess.py data raw_data.csv

# create exploratory data analysis figures
results/corr_figure.png results/quality_distributions_figure.png: data/test_df.feather data/train_df.feather data/raw_data.csv
	python src/eda_figures.py data raw_data.csv results

# fit, tune and test model
results/weights_figure.png results/initial_crossval_results.feather results/tuned_crossval_results.feather: data/test_df.feather data/train_df.feather 
	python src/model_fitting.py data results

# render final report
doc/white_wine_predict_report.md doc/white_wine_predict_report.html: doc/references_white_wine.bib doc/white_wine_predict_report.Rmd
	Rscript -e "rmarkdown::render('doc/white_wine_predict_report.Rmd', output_format = 'github_document')"
	
clean: 
	rm -rf data
	rm -rf results
	rm -rf doc/white_wine_predict_report.md doc/white_wine_predict_report.html	