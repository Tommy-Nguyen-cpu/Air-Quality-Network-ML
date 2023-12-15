import pandas as pd
import numpy as np
import os
import glob
from datetime import *
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from statsmodels.tsa.arima.model import ARIMA

def make_dataset(data, shift=1):
  total_window_size = len(data) + shift
  data = np.array(data, dtype=np.float32)
  ds = tf.keras.utils.timeseries_dataset_from_array(
      data=data,
      targets=None,
      sequence_length=total_window_size,
      sequence_stride=1,
      shuffle=True,
      batch_size=32,)

  return ds

def CleanData(df):
  naDropped = df.dropna(subset = ['parameter'])
  naDropped['timestamp'] = pd.to_datetime(naDropped['timestamp'])
  data_pivoted = pd.pivot_table(naDropped, index=["timestamp", "device_id", 'latitude', 'longitude'], values="value", columns="parameter")
  data_pivoted.reset_index(inplace=True)
  mask = data_pivoted['device_id'] != data_pivoted['device_id'].shift()
  time_diff = (data_pivoted['timestamp'] - data_pivoted['timestamp'].shift()).fillna(pd.Timedelta(seconds=0))
  data_pivoted['time_diff_Group'] = (time_diff > pd.Timedelta(seconds=30)).cumsum()
  data_pivoted["DiffID"] = mask.cumsum()

  result = data_pivoted.groupby(['DiffID', 'time_diff_Group']).agg({'device_id':'first', 'timestamp':'first','Humidity': 'first', 'Temperature': 'first', 'PM 1': 'first', 'PM 2.5': 'first', 'PM 10': 'first', 'longitude':'first', 'latitude':'first'})
  result['PM 1'].fillna(value=result['PM 1'].mean(), inplace=True)
  result['PM 2.5'].fillna(value=result['PM 2.5'].mean(), inplace=True)
  result['PM 10'].fillna(value=result['PM 10'].mean(), inplace=True)
  result['Humidity'].fillna(value=result['Humidity'].mean(), inplace=True)
  result['Temperature'].fillna(value=result['Temperature'].mean(), inplace=True)
  # result['timestamp'] = result['timestamp'].map(pd.Timestamp.timestamp)
  result.reset_index(inplace=True)
  result.set_index('timestamp', inplace=True)
  return result

def Predict(myDataset, columnToPredict):
    time_series = myDataset[columnToPredict].asfreq('30s')
    time_series.fillna(value=time_series.mean(), inplace=True)
    model = ARIMA(time_series,  # train on data up to "today"
                    order=(2, 0, 0),
                    seasonal_order=(0, 1, 1, 7))

    fit_model = model.fit()
    return fit_model.forecast()[0]

if __name__ == "__main__":
    # Assuming we have our code mounted to a drive, this example should work. Otherwise, replace with dir to actual file.
    data = pd.read_csv(f'drive/MyDrive/Hackathon - Air Quality Notebooks/HackathonProvidedCSV/data01_short.csv', sep=',')

    # Preps data for ARIMA model.
    myDataset = CleanData(data)
    
    Predict(myDataset, "PM 1")