'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

def create_felony_charge(arrest_events):
    '''Create a dataframe indicating if an arrest has a felony charge.
    
    Parameters: 
        arrest_events (DataFrame): DataFrame containing arrest events with a 'charge_degree' column.
    
    Returns:
        DataFrame: DataFrame with 'arrest_id' and 'has_felony_charge' columns.
    '''
    felony_charge = arrest_events.groupby('arrest_id').apply(
        lambda x: pd.Series({'has_felony_charge': (x['charge_degree'] == 'felony').any()})).reset_index()
    
    return felony_charge


# 2. Merge `felony_charge` with `pre_universe` into a new dataframe
def merge_felony_charge(pred_universe, felony_charge):
    '''Merge the felony charge information with the prediction universe.
    
    Parameters:
        pred_universe (DataFrame): DataFrame containing prediction universe.
        felony_charge (DataFrame): DataFrame with felony charge information.
    
    Returns:
        DataFrame: Merged DataFrame with felony charge information.
    '''
    # Merge the felony charge information with the prediction universe
    # on 'arrest_id' using an outer join to include all records from both dataframes
    merge_felony_charge = pd.merge(pred_universe, felony_charge, on='arrest_id', how='outer')

    return merge_felony_charge

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def cat_plot(pred_universe_merged):
    '''Create a categorical plot for felony rearrest predictions.
    
    Parameters:
        pred_universe_merged (DataFrame): DataFrame containing prediction universe with felony charge information.
    
    Returns:
        None: Saves the plot as a PNG file.
    '''
    sns.catplot(data=pred_universe_merged, 
                 x='has_felony_charge', 
                 y='prediction_felony', 
                 kind='bar')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest.png', bbox_inches='tight')
    plt.close('all')

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?
def cat_plot_nonfelony(pred_universe_merged):
    '''Create a categorical plot for non-felony rearrest predictions.
    
    Parameters:
        pred_universe_merged (DataFrame): DataFrame containing prediction universe with felony charge information.
    
    Returns:
        None: Saves the plot as a PNG file.
    '''
    sns.catplot(data=pred_universe_merged, 
                 x='has_felony_charge', 
                 y='prediction_nonfelony', 
                 kind='bar')
    plt.savefig('./data/part4_plots/catplot_nonfelony_rearrest.png', bbox_inches='tight')
    plt.close('all')

    print("The difference between the plots may be explained by the fact that individuals with felony charges are generally considered to have a higher risk of reoffending, which is reflected in the higher predicted probabilities for felony rearrest compared to non-felony rearrest.")


# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
def cat_plot_hue(pred_universe_merged):
    '''Create a categorical plot with hue for felony rearrest predictions.
    
    Parameters:
        pred_universe_merged (DataFrame): DataFrame containing prediction universe with felony charge information.
    
    Returns:
        None: Saves the plot as a PNG file.
    '''
    sns.catplot(data=pred_universe_merged, 
                 x='has_felony_charge', 
                 y='prediction_felony', 
                 hue='has_felony_charge', 
                 kind='bar')
    plt.savefig('./data/part4_plots/catplot_felony_rearrest_hue.png', bbox_inches='tight')
    plt.close('all')

    print("The higher predicted probability for arrestees with a current felony charge who did not get rearrested for a felony crime compared to those with a misdemeanor charge who did get rearrested suggests that the model may be capturing the inherent risk associated with felony charges, even if the individual did not reoffend. This indicates that the model is sensitive to the severity of charges rather than just past behavior.")