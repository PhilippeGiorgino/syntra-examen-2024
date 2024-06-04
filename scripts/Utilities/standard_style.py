import matplotlib.pyplot as plt
from matplotlib import rcParams

BLUE = '#1D366F'
GREEN = '#08C075'

def standard_style():
    """
    Function to set standard plotting parameters.

    Args:
        directory_path (str): The path to the folder containing JSON files.
        location (str): The name of the location to add to the 'location' column.

    Returns:
        pandas.DataFrame: A DataFrame that contains all the data from the JSON files,
                          with an extra column 'location'.
    """

    rcParams['axes.spines.top'] = False
    rcParams['axes.spines.right'] = False
    rcParams['figure.figsize'] = (14, 6)
    rcParams['lines.linewidth'] = 3
    rcParams['axes.prop_cycle'] = plt.cycler(color=[BLUE, GREEN])
    rcParams['legend.frameon'] = False
    rcParams['font.size'] = 16
    return