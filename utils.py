from datetime import date,datetime,timedelta
import pandas as pd
import numpy as np
import requests, json

def gen_alloc_data(ticker, allocation):
        return {'ticker' : ticker,
                'alloc' : allocation}

def allocs_to_frame(json_allocations):

        alloc_list = []

        for json_alloc in json_allocations:
            allocs = pd.DataFrame(json_alloc['allocations'])
            allocs.set_index('ticker', inplace=True)
            alloc_serie = allocs['alloc']
            alloc_serie.name = json_alloc['date'] 
            alloc_list.append(alloc_serie)

        try:
            all_alloc_df = pd.concat(alloc_list, axis=1).T
        except ValueError:
            all_alloc_df = pd.DataFrame()
        finally:
            return all_alloc_df