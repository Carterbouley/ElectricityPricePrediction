# import dotenv
# from dotenv import load_dotenv
# import os
# load_dotenv()

import requests
import pandas as pd

class WeatherGetter():
    
    def __init__(self):
        self.BASE_URL = 'https://api.darksky.net/'
        self.SECRET_KEY = os.getenv("DARKSKY_KEY")
        
    def weather_getter(self, time):
        forcast = requests.get(f"https://api.darksky.net/forecast/{self.SECRET_KEY}/51.5074,0.1278,{time}")
        return forcast
    
    
    
class Battery():
    
    def __init__(self, dataset):
        self.dataset = dataset
        
    
    def charging(self, data):
      
        three_cheapest_hours = data.nsmallest(3)
        self.dataset.loc[three_cheapest_hours.index, 'Charge Status'] = 'charging'
        
        return self.dataset
        
    
    def discharging(self, data):
        for t in range(52560, 61327, 24):
            three_most_expensive_hours = data['GBP/mWh'][t:t+23].nlargest(3)
            self.dataset.loc[three_most_expensive_hours.index, 'Charge Status'] = 'discharging'
        return self.dataset
        
        
class Cleaning():
    
    def __init__(self):
        pass
    
    def clean_df(self, df):
        
        df = pd.DataFrame(df[0])
        df.columns = df.columns.droplevel()
        df.columns = df.columns.droplevel()
    
        df = df.rename(columns = {'Unnamed: 0_level_2' : 'Date', 'Hours':'UK_time', 'UK': 'GBP/mWh', 'CET time': 'CET/CEST time'})
        df['GBP/mWh'] = df['GBP/mWh']/100
    
        return df
    
    def datetime_fixer(self, result):
        
        result['datetime'] = result['Date'] + '-'+ result['CET/CEST time']
        result['datetime'] = result.apply(lambda x: x['datetime'][:10] + x['datetime'][-3:], axis = 1)
        result['datetime'] = result['datetime'].shift(+2)
        result['datetime'] = result['datetime'] + ':00:00'
        result.drop(result.loc[result['GBP/mWh'].isna()].index, inplace = True)
        result.drop(result.loc[result['datetime'].duplicated()].index, inplace = True)
        result = result.drop(columns = ['Date', 'UK_time', 'CET/CEST time'])

        result['datetime'] = pd.to_datetime(result['datetime'], dayfirst = True)
        result.set_index('datetime', inplace = True)
        result = result.iloc[1:]
        
        return result
    
    def nn_result_to_df(self, Y_pred, X_test):
        last_list=[]

        for i in range (0, len(Y_pred)):
            last_list.append((Y_pred[i][0][23]))

        actual = pd.DataFrame((X_test[:,0]))
        actual.rename(columns = {0:'actual'}, inplace = True)
        actual['predictions'] = last_list
        actual['difference'] = (actual['predictions'] - actual['actual']).abs()
        actual['difference_percentage'] = ((actual['difference'])/(actual['actual']))*100
        
        return actual
    
class Graphs():
    
    def __init__(self):
        pass
    
    def clean_for_viz(self, df):
        df.drop(columns = ['Open', 'High', 'Low', 'Vol.'], inplace = True)
        df['datetime'] = pd.to_datetime(df['Date'])
        df = df.set_index('datetime')
        df = df.drop(columns = 'Date')
        df = df.iloc[::-1]
        
        return df
    