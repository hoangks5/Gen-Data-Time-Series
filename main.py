# Load and preview dataset
import datetime
from pickle import load
import pandas as pd
import numpy as np
import matplotlib.pyplot

day = 24 * 60 * 60
year = 365.2425 * day


def load_dataframe() -> pd.DataFrame:
    """ Create a time series x sin wave dataframe. """
    df = pd.DataFrame(columns=['date', 'sin'])
    df.date = pd.date_range(start='2018-01-01', end='2021-03-01', freq='D')
    df.sin = 1 + np.sin(df.date.astype('int64') // 1e9 * (2 * np.pi / year))
    df.sin = (df.sin * 100).round(2)
    df.date = df.date.apply(lambda d: d.strftime('%Y-%m-%d'))
    return df

train_df = load_dataframe()
print(train_df)