from datetime import datetime, timedelta, date
import pandas as pd
import numpy as np
import requests, json
from api import API

class MarketData():
    __competi = API.competi()
    __user_key = API.user_key()
    __url_base = API.url_base()
    
    def __init__(self, market, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day):
        assert market in ["IBEX", "DAX", "EUROSTOXX"]
        
        try:
            self.__date = date(int(year), int(month), int(day))
        except ValueError as exc:
            raise ValueError(exc.args)
        
        self.__market_name = market
        self.__ticker_master = API.ticker_master(self.__market_name)
        self.__stocks = self.__ticker_master['ticker']
        self.__initialize_attributes()
        self.__ohlcv()
        
        if (self.__date == datetime.now().date()):
            self.__date = datetime.now().date() - timedelta(days=1)
            
    def __stocks_date(self, dataframe):
      
        date_str = self.__date.strftime("%Y-%m-%dT%H:%M:%S")
        end_date_condition = (self.__ticker_master['end_date'] >= date_str) | (self.__ticker_master['end_date'] == "")
        boolean_condition = (self.__ticker_master['start_date'] <= date_str) & (end_date_condition)
        stocks_date = self.__ticker_master[boolean_condition]['ticker']
        
        return dataframe.loc[:, stocks_date]
        
    def __ohlcv(self): 
        for stock in self.__stocks:
            historical_data = API.historical_data(stock, self.__market_name)
            self.__open = pd.concat([self.__open, historical_data['open']], axis=1)
            self.__high = pd.concat([self.__high, historical_data['high']], axis=1)
            self.__low = pd.concat([self.__low, historical_data['low']], axis=1)
            self.__close = pd.concat([self.__close, historical_data['close']], axis=1)
            self.__volume = pd.concat([self.__volume, historical_data['vol']], axis=1)
            
        self.__rename_columns()
        self.__establish_dataframes_index_as_datetime()
        
    def __rename_columns(self):
        self.__open.columns = self.__stocks
        self.__high.columns = self.__stocks
        self.__low.columns = self.__stocks
        self.__close.columns = self.__stocks
        self.__volume.columns = self.__stocks

    def __establish_dataframes_index_as_datetime(self):
        self.__open.index = pd.to_datetime(self.__open.index)
        self.__high.index = pd.to_datetime(self.__high.index)
        self.__low.index = pd.to_datetime(self.__low.index)
        self.__close.index = pd.to_datetime(self.__close.index)
        self.__volume.index = pd.to_datetime(self.__volume.index)

    def __initialize_attributes(self):
        self.__open = pd.DataFrame()
        self.__high = pd.DataFrame()
        self.__low = pd.DataFrame()
        self.__close = pd.DataFrame()
        self.__volume = pd.DataFrame()
    
    def get_ohlc(self):
        return self.__open, self.__high, self.__low, self.__close

    def get_open(self):
        return self.__stocks_date(self.__open)

    def get_high(self):
        return self.__stocks_date(self.__high)
    
    def get_low(self):
        return self.__stocks_date(self.__low)

    def get_close(self):
        return self.__stocks_date(self.__close)
    
    def get_volume(self):
        return self.__stocks_date(self.__volume)

    def get_date(self):
        return self.__date.strftime("%Y-%m-%d")
    
    def get_year(self):
        return str(self.__date.year) 

    def get_month(self):
        return str(self.__date.month)

    def get_day(self):
        return str(self.__date.day)

    def get_market_name(self):
        return self.__market_name
    
    def set_date(self, year, month, day):
        try:
            self.__date = date(int(year), int(month), int(day))
        except ValueError as exc:
            raise ValueError(exc.args)