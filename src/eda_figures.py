from src.download_data import download_data
from src.preprocess import preprocess_data
import pandas as pd
import altair as alt
import os

def make_eda_figures(data_folder, results_folder):
    """Function for preparing and saving the figures used for the eda analysis of the white wine dataset

    Parameters:
    data_folder (str): raw data directory
    results_folder (str): directory to save results in

    Returns:
    
    Example:
    make_eda_figures('data', 'results')

   """
    # Call download data script
    download_data(data_folder, 'raw_data.csv')
    white_wine_df = pd.read_csv(os.path.join(data_folder, 'raw_data.csv'), index_col=0)
    
    # Call preprocess script
    X_train, X_test, y_train, y_test = preprocess_data('data/raw_data.csv')
    
    # Make first figure (the distributions for quality)
    y_train_chart = alt.Chart(pd.DataFrame(y_train), title='Train data').mark_bar(size=55).encode(
        x=alt.X('quality', axis=alt.Axis(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        y='count()'
    )

    y_test_chart = alt.Chart(pd.DataFrame(y_test), title='Test data').mark_bar(size=55).encode(
        x=alt.X('quality', axis=alt.Axis(values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])),
        y='count()'
    )

    quality_distributions = (y_train_chart | y_test_chart)
    
    # Make second figure
    cor_data = (white_wine_df.corr().stack()
                  .reset_index()
                  .rename(columns={0: 'correlation', 'level_0': 'variable', 'level_1': 'variable2'}))
    cor_data['correlation_label'] = cor_data['correlation'].map('{:.2f}'.format)  # Round to 2 decimal

    base = alt.Chart(cor_data).encode(
        x='variable2:O',
        y='variable:O'    
    )

    # Text layer with correlation labels
    # Colors are for easier readability
    text = base.mark_text().encode(
        text='correlation_label',
        color=alt.condition(
            alt.datum.correlation > 0.5, 
            alt.value('white'),
            alt.value('black')
        )
    )

    # The correlation heatmap itself
    cor_plot = base.mark_rect().encode(
        alt.Color('correlation:Q', scale=alt.Scale(domain=(-1, 1), scheme='purpleorange'))
    )

    cor_plot_text = (cor_plot + text).properties(height=600, width = 600).configure_axis(labelFontSize = 16
    ).configure_legend(titleFontSize = 15)
    
    # Save figures in html (png was giving me errors for saving?)
    if not os.path.isdir(results_folder):
        os.mkdir(results_folder) 
        quality_distributions.save(os.path.join(results_folder, 'quality_distributions_figure.html'))
        cor_plot_text.save(os.path.join(results_folder, 'corr_figure.html'))
    

