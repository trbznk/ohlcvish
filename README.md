# ohlcvish

`ohlcvish` takes **OHLCV** data, generate multiple technical indicators on it and the corresponding *Buy-Hold-Sell* signal.

## Usage

To use `ohlcvish` you need your OHLCV data to be in a [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) like this:

```python
import pandas as pd

btc = pd.read_csv("BTCUSD.csv")
print(btc.head())
```

```txt
      date    open    high     low   close      volume
2014-11-28  363.59  381.34  360.57  376.28  3220878.18
2014-11-29  376.42  386.60  372.25  376.72  2746157.05
2014-11-30  376.57  381.99  373.32  373.34  1145566.61
2014-12-01  376.40  382.31  373.03  378.39  2520662.37
2014-12-02  378.39  382.86  375.23  379.25  2593576.46
```

Use `ohlcvish()` function to get all signals (`1=buy, 0=hold, -1=sell`):

```python
btc = ohlcvish(btc)
print(btc)
```

```txt
      date  macd  rsi  stoch  adx  aroon  bbands  sar  ma
2020-07-13     0    0      0    0      0       0    0   0
2020-07-14     0    0      0    0      0       0    0   0
2020-07-15     0    0      0    0      0       0    0   0
2020-07-16     0    0      0    0      0       0    0   0
2020-07-17    -1    0      0    0      0       0    0  -1
2020-07-18     0    0      0    0      0       0    0   0
2020-07-19     1    0      0    0      0       0    0   0
2020-07-20    -1    0      0    0      1       0    0   0
2020-07-21     1    0      0    0      0       0    1   0
2020-07-22     0    0      0    0      0      -1    0   1
2020-07-23     0    0      0    0      0       0    0   0
2020-07-24     0    0      0    0      0       0    0   0
2020-07-25     0    0     -1    0      0      -1    0   0
2020-07-26     0    0      0    0      0       0    0   0
2020-07-27     0    0      0    0      0       0    0   0
2020-07-28     0    0      0    0      0       0    0   0
2020-07-29     0    0      0    0      0       0    0   0
2020-07-30     0    0      0    0      0       0    0   0
2020-07-31     0    0      0    0      0       0    0   0
2020-08-01     0    0      0    0      0      -1    0   0
```
