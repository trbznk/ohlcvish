ohlcvish
========

`ohlcvish` takes **OHLCV** data, generate multiple technical indicators on it and then gives you all existing *Buy-Hold-Sell* combinations in the dataset.

## How to use

To use `ohlcvish` you need your OHLCV data to be in a [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) like this:

```python
import pandas as pd

eth = pd.read_csv("data/ETH.csv", index_col="datetime", parse_dates=True)

eth.head()
```

```
            close  high     low    open   volume
datetime                                        
2015-08-07   3.00   3.0  0.6747  0.6747   123.93
2015-08-08   1.20   3.0  0.1500  3.0000  2119.43
2015-08-09   1.20   1.2  1.2000  1.2000     0.00
2015-08-10   1.20   1.2  1.2000  1.2000     0.00
2015-08-11   0.99   1.2  0.6504  1.2000  9486.09
```

Use `ohlcvish()` function to get all signals:

```python
from ohlcvish import ohlcvish

signals = ohlcvish(eth)

signals.head()
```

```
   macd  rsi  stoch  adx  aroon  bbands  sar  ma  amount  forecast_mean  forecast_median  forecast_min  forecast_max
0    -1   -1      0    0      0       0   -1   0       1      59.947906        59.947906     59.947906     59.947906
1    -1    0      0   -1     -1       0    0   0       1      -2.904930        -2.904930     -2.904930     -2.904930
2    -1    0      0   -1      0       0   -1   0       3      -7.415414        -6.642701    -11.645688     -3.957853
3    -1    0      0   -1      0       0    0   0       1     298.919554       298.919554    298.919554    298.919554
4    -1    0      0    0     -1       1   -1  -1       1     -54.082750       -54.082750    -54.082750    -54.082750
```


