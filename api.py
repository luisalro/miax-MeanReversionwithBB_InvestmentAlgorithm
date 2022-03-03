from datetime import date,datetime,timedelta
import pandas as pd
import numpy as np
import requests, json

class API():    
    
    @staticmethod
    def competi():
        return 'mia_4'
    
    @staticmethod
    def user_key():
        return 'AIzaSyBIAVe1BIJaxb-LVyMYMmhtoPPdJZSfRqI'
    
    @staticmethod
    def url_base():
        return 'https://miax-gateway-jog4ew3z3q-ew.a.run.app'

    @staticmethod
    def ticker_master(market):
        
        assert market in ["IBEX", "DAX", "EUROSTOXX"]
        
        url = f'{API.url_base()}/data/ticker_master'
        
        params = {'competi': API.competi(),
                  'market': market,
                  'key': API.user_key()}

        response = requests.get(url, params)
        tk_master = response.json()
        
        return pd.DataFrame(tk_master['master'])
        

    @staticmethod
    def historical_data(ticker, market):

        
        assert market in ["IBEX", "DAX", "EUROSTOXX"]
        
        url = f'{API.url_base()}/data/time_series'
    
        params = {'market': market,
                  'key': API.user_key(),
                  'ticker': ticker,
                  'close': False}

        response = requests.get(url, params)
        tk_data = response.json()
    
        return pd.read_json(tk_data, typ='frame')
    