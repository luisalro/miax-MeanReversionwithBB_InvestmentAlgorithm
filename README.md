This lab was created by Guillermo Melendez , professor from mIA-X master's degree at BME Institute. Scripts can be programmed in either Python or R.

### Instructions

## Input

From the BME endpoint you will be able to download the daily stock data, indicating the index, the ticker and the date range that you need (with this you will obtain the data of all the assets of IBEX, DAX or EUROSTOXX indexes). The data are homogenized, adjusted and without survivorship bias. 

## Execution

As of 31/3/20, we execute the algorithm daily, sending the resulting orders to the broker in order to . We will send the orders before the opening (between 7 and 9 in the morning). 

## Output

The output is similar to an index, or an ETF. On a daily basis, we indicate the percentage of capital in which we want to be invested for each asset in the index. All sales operations will be carried out at the opening auction. All purchase operations will be carried out at the closing auction. We will send the orders before the opening (between 7 and 9 in the morning).


Note: All the orders have been sent during COVID 19 crisis, a black swan event. Please check the Mean Reversion systems during COVID-19 (Black Swan event) presentation in order to see the results, conclusions and further steps (use of computing to enhance in order to optimize the portfolio).

### Deliverable

The algorithm will consist of a mean reversion with Bollinger Bands allocator trading strategy used on IBEX. It will be coded in Python.

A mean reversion trading strategy involves betting that prices will revert back towards the mean or average. Markets are forever moving in and out of phases of mean reversion and momentum. Therefore it’s possible to develop strategies for both types of market. A simplistic example of a mean reversion strategy is to buy a stock after it has had a large fall in price. When a stock has seen a big drop, there’s usually a good chance that it will bounce back to a more normal level.


