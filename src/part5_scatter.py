'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatterplot_felony_nonfelony(pred_universe):
    '''
    Creates a scatter plot of felony vs non-felony predictions with hue by felony charge.

    Parameters:
    - pred_universe: DataFrame containing prediction data.

    Returns:
    - None: Saves the plot as a PNG file.
    '''
    sns.lmplot(data=pred_universe, 
               x='prediction_felony', 
               y='prediction_nonfelony', 
               hue='has_felony_charge')
    plt.savefig('./data/part5_plots/scatter_felony_nonfelony.png', bbox_inches='tight')
    plt.close('all')

    print("The group of dots on the right side of the plot represents individuals with high predictions for felony rearrest,\
           indicating they are at a higher risk of reoffending.")


# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatterplot_felony_rearrest(pred_universe):
    '''
    Creates a scatter plot of felony rearrest predictions vs actual rearrest status.

    Parameters:
    - pred_universe: DataFrame containing prediction data.

    Returns:
    - None: Saves the plot as a PNG file.
    '''
    sns.scatterplot(data=pred_universe, 
                    x='prediction_felony', 
                    y='y_felony')
    plt.savefig('./data/part5_plots/scatter_felony_rearrest.png', bbox_inches='tight')
    plt.close('all')

    print("The plot suggests that the model may not be well-calibrated, as there are many instances where high predictions do not \
          correspond to actual rearrests, indicating potential overestimation of risk.")