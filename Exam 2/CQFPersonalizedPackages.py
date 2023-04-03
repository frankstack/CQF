# Kannan Singaravelu
# https://github.com/kannansingaravelu
# Helper functions to plot binomial tree
# Save the file as '.py' on the same location 

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

## Base packages
import matplotlib
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm, gmean
import matplotlib.pyplot as plt
from numpy.linalg import multi_dot

# Import cufflinks
import cufflinks as cf
cf.set_config_file(
    offline=True, 
    dimensions=((1000,600)),
    theme= 'henanigans')

# Import plotly express for EF plot
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
px.defaults.template = "plotly_dark"
px.defaults.width = 950
px.defaults.height = 600

# Plot settings
plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = [12.0, 8.0]
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['lines.linewidth'] = 2.0

# Set max row to 300
pd.set_option('display.max_rows', 300)
    