import numpy as np
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_absolute_error

## import tensorflow as tf
## from prophet import Prophet
## from xgboost import XGBRegressor

sns.set_theme(style="whitegrid")