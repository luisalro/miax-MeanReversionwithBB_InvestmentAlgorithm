class API():    
    @staticmethod
    def get_competi():
        return 'mia_4'
    
    @staticmethod
    def get_user_key():
        return 'AIzaSyCWjvfiRkwssq-LX0Gwy6nsLfznrE44fuw'
    
    @staticmethod
    def get_url_base():
        return 'https://miax-gateway-jog4ew3z3q-ew.a.run.app'

    @staticmethod
    def get_ticker_master(market):
        
        """
          Retrieves the ticker master of a market.

          Parameters
          ----------
              market (str) : market to retrieve the data from. It must be IBEX, DAX or EUROSTOXX.

          Returns
          --------
              pd.DataFrame : the ticker master of the market.
        """
        
        assert market in ["IBEX", "DAX", "EUROSTOXX"], "Not a valid market. The market must be IBEX, DAX or EUROSTOXX"
        
        url = f'{API.get_url_base()}/data/ticker_master'
        
        params = {'competi': API.get_competi(),
                  'market': market,
                  'key': API.get_user_key()}

        response = requests.get(url, params)
        tk_master = response.json()
        
        return pd.DataFrame(tk_master['master'])
        

    @staticmethod
    def get_price_series(ticker, market):
        """
           Retrieves the price series of a stock.

           Parameters
           ----------
               ticker (str) : stock to retrieve the data from.
               market (str) : market to which the stock belongs. It must be IBEX, DAX or EUROSTOXX.

           Returns
           -------
               pd.DataFrame : the ohlcv of the stock.
        """
        
        assert market in ["IBEX", "DAX", "EUROSTOXX"], "Not a valid market. The market must be IBEX, DAX or EUROSTOXX"
        
        url = f'{API.get_url_base()}/data/time_series'
    
        params = {'market': market,
                  'key': API.get_user_key(),
                  'ticker': ticker,
                  'close': False}

        response = requests.get(url, params)
        tk_data = response.json()
    
        return pd.read_json(tk_data, typ='frame')
    
    @staticmethod
    def get_benchmark_series(market):
        """
           Retrieves the price series of a benchmark.

           Parameters
           ----------
               market (str) : market which corresponds to our benchmark. It must be IBEX, DAX or EUROSTOXX.
               
           Returns
           -------
               pd.DataFrame : the ohlcv of the benchmark.
        """
        
        assert market in ["IBEX", "DAX", "EUROSTOXX"], "Not a valid market. The market must be IBEX, DAX or EUROSTOXX"
        
        url = f'{API.get_url_base()}/data/time_series'
        
        params = {'market':market,
                'key':API.get_user_key(),
                'ticker':'benchmark',
                'close':False}
        
        response=requests.get(url, params)
        tk_data=response.json()
        
        return pd.read_json(tk_data, typ='frame')
    
