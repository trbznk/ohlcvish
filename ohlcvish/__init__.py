import pandas as pd
import copy

from tqdm import tqdm

from .preprocess import preprocess


name = "ohlcvish"

AGGREGATING_FUNCTIONS = [
    "count",
    "mean",
    "median",
    "min",
    "max"
]


def ohlcvish(data, forecast_period=30):
    if type(data) == list:
        ohlcvs = copy.deepcopy(data)
    else:
        ohlcvs = [copy.deepcopy(data)]
    
    featured_ohlcvs = []

    for ohlcv in tqdm(ohlcvs, desc="preprocess"):
        featured_ohlcvs.append(preprocess(ohlcv,
                                          forecast_period=forecast_period))

    signals = pd.concat(featured_ohlcvs)
    cols = [col for col in signals.columns.tolist() if "forecast" not in col]
    signals = signals.groupby(cols).agg({"forecast": AGGREGATING_FUNCTIONS})
    signals = signals.reset_index()

    new_columns = []
    for col1, col2 in signals.columns.ravel():
        if col2 == "":
            new_column = col1
        else:
            new_column = f"{col1}_{col2}"
        if new_column == "forecast_count":
            new_column = "amount"
        new_columns.append(new_column)
    signals.columns = new_columns
    return signals
     