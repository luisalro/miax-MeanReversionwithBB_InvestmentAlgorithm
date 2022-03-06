from datetime import datetime, timedelta, date
import pandas as pd
import numpy as np
import requests, json
from api import API

class Market():
    __competi = API.get_competi()
    __user_key = API.get_user_key()
    __url_base = API.get_url_base()
    
    def __init__(self, market, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day):
        assert market in ["IBEX", "DAX", "EUROSTOXX"], "Not a valid market. The market must be IBEX, DAX or EUROSTOXX"
        
        try:
            self.__date = date(int(year), int(month), int(day))
        except ValueError as exc:
            raise ValueError(exc.args)
        
        self.__market_name = market
        self.__ticker_master = API.get_ticker_master(self.__market_name)
        self.__stocks = self.__ticker_master['ticker']
        self.__initialize_attributes()
        self.__ohlcv()
        
        # Get previous day in case the market is closed today
        if (self.__date == datetime.now().date()):
            self.__date = datetime.now().date() - timedelta(days=1)
        
    def __ohlcv(self): 
        for stock in self.__stocks:
            price_series = API.get_price_series(stock, self.__market_name)
            self.__open = pd.concat([self.__open, price_series['open']], axis=1)
            self.__high = pd.concat([self.__high, price_series['high']], axis=1)
            self.__low = pd.concat([self.__low, price_series['low']], axis=1)
            self.__close = pd.concat([self.__close, price_series['close']], axis=1)
            self.__volume = pd.concat([self.__volume, price_series['vol']], axis=1)
            
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
        return self.__open

    def get_high(self):
        return self.__high
    
    def get_low(self):
        return self.__low

    def get_close(self):
        return self.__close
    
    def get_volume(self):
        return self.__volume

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
