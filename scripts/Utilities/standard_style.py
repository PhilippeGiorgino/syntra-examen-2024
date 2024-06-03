import matplotlib.pyplot as plt
from matplotlib import rcParams

BLUE = '#1D366F'
GREEN = '#08C075'

def standard_style():

    rcParams['axes.spines.top'] = False
    rcParams['axes.spines.right'] = False
    rcParams['figure.figsize'] = (14, 6)
    rcParams['lines.linewidth'] = 3
    rcParams['axes.prop_cycle'] = plt.cycler(color=[BLUE, GREEN])
    rcParams['legend.frameon'] = False
    rcParams['font.size'] = 16
    return