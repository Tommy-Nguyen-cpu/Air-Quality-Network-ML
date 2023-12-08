import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

from io import StringIO


model = tf.keras.models.load_model('./airQ_ml/AirQModel.h5')
# model.summary()

class File:
    def __init__(self, filename, cols, data):
        self.filename = filename
        self.cols = cols
        self.data = data
        self.get_df()
        self.predict()
    
    def get_df(self):
        self.df = pd.read_csv(
            StringIO('\n'.join(self.data)),
            sep = ',',
            header = None,
            names = self.cols,
        )

    def clean_data(self):
        df = self.df
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values("timestamp")

        grouped = self.group_deviceID_rows(df)
        grouped['parameter'] = grouped['parameter'].apply(np.array)
        grouped['value'] = grouped['value'].apply(np.array)
        return grouped

    def group_deviceID_rows(self, df, MinSampleRate = 31, MaxSampleRate = 32):
        grouped2 = (
            df.groupby(
                ['device_id', pd.Grouper(key='timestamp', freq=f'30s')]
                ).agg({
                'parameter': list,
                'value': list,
                'latitude': max,
                'longitude': max
            }).reset_index())

        grouped2 = grouped2[grouped2['value'].str.len() == 5]
        for i in range(MinSampleRate, MaxSampleRate):
            temp = (self.df.groupby(
                ['device_id', pd.Grouper(key='timestamp', freq=f'{i}s')]
                ).agg({
                    'parameter': list,
                    'value': list,
                    'latitude': max,
                    'longitude': max
                }).reset_index())
            grouped2 = pd.concat(
                [grouped2, temp[temp['value'].str.len() == 5]]
            )
        return grouped2

    def predict(self):
        df = self.clean_data()
        valueNP = np.vstack(df['value'].to_numpy())
        pred = model.predict(valueNP[:, 3:5])
        self.pred = pd.DataFrame(pred, columns=['Predicted PM 1', 'Predicted PM 2.5', 'Predicted PM 10'])
        self.pred['Humidity'] = valueNP[:, 3]
        self.pred['Temperature'] = valueNP[:, 4]

