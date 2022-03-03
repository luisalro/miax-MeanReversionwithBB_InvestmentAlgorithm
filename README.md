# miax-mean_reversion_bb_algo

This exercise was created by Guillermo Melendez , professor from mIA-X master's degree at BME Institute. Scripts can be programmed in either Python or R.

### Instructions

From the BME end point you will be able to download the daily stock data, indicating the index, the ticker and the date range that you need (with this you will obtain the data of all the assets of IBEX, DAX or EUROSTOXX indexes). The data are homogenized, adjusted and without survivorship bias. 

### During algorithm development:

Until 30/3/20 you will be able to send the complete history of orders and see the evolution of the algorithm in order to decide whether which algorithm to use.

### During exercise evaluation:

As of 31/3/20, every day you will need to execute the algorithm sending the resulting ordersto BME end point. You must send the orders before the opening (between 7 and 9 in the morning). 

The output would be similar to an index, or an ETF.

Every day you have to indicate the percentage of capital in which you want to be invested for each asset of the index.

If you want to maintain the proportion, you don't need to send anything. Only when you want to rebalance.

All sales operations will be carried out at the opening auction.

All purchase operations will be carried out in a closing auction.

Note: All the orders have been sent during COVID 19 crisis.

### Deliverable

The algorithm will consist of a mean reversion with Bollinger Bands trading strategy coded in Python.

A mean reversion trading strategy involves betting that prices will revert back towards the mean or average. Markets are forever moving in and out of phases of mean reversion and momentum. Therefore it’s possible to develop strategies for both types of market. A simplistic example of a mean reversion strategy is to buy a stock after it has had a large fall in price. When a stock has seen a big drop, there’s usually a good chance that it will bounce back to a more normal level.


