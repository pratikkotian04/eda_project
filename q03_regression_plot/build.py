# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your code here
var1='GrLivArea'
var2='Saleprice'
def regression_plot(var1,var2):
    sns.lmplot(var1)





