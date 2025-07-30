'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def bar_plot(pred_universe):
    '''
    Produces a bar plot with the counts of the fta column in the pred_universe dataframe.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Bar plot of fta counts
    '''
    # Prepare the data
    fta_counts = pred_universe.groupby(['fta']).size().reset_index(name='count')

    sns.barplot(data=fta_counts, 
                x='fta', 
                y='count')
    plt.savefig('./data/part3_plots/barplot_fta.png', bbox_inches='tight')

# 2. Hue the previous barplot by sex
def bar_plot_with_hue(pred_universe):
    '''
    Produces a bar plot with the counts of the fta column separated by sex in the pred_universe dataframe.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Bar plot of fta counts with hue based on sex
    '''

    # Prepare the data
    fta_count_sex = pred_universe.groupby(['fta', 'sex']).size().reset_index(name='count')

    sns.barplot(data=fta_count_sex, 
                x='fta', 
                y='count',
                hue='sex')
    plt.savefig('./data/part3_plots/barplot_fta_hue.png', bbox_inches='tight')
    plt.close('all')
    
# 3. Plot a histogram of age_at_arrest
def histogram(pred_universe):
    '''
    Produces a histogram based on the age_of_arrest.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram of age_at_arrest
    '''
    sns.histplot(data=pred_universe, 
                 x='age_at_arrest', 
                 bins=24)
    plt.savefig('./data/part3_plots/histogram.png', bbox_inches='tight')
    plt.close('all')

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_group(pred_universe):
    '''
    Produces a histogram based on the age_of_arrest by age groups.

    Parameters:
    - pred_universe dataframe

    Returns:
    - Histogram of age_at_arrest by specified age groups.
    '''
    age_bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe,
                    x='age_at_arrest', 
                    bins=age_bins)
    plt.savefig('./data/part3_plots/histogram_age_group.png', bbox_inches='tight')
    plt.close('all')
