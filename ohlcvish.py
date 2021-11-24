import pandas as pd
import talib
import numpy as np

# TODO: refactor function parameters to constants


def macd(df):
    df["macd"], df["macdsignal"], df["macdhist"] = talib.MACD(df["close"],
                                                              fastperiod=12,
                                                              slowperiod=26,
                                                              signalperiod=9)
    df["macdcut"] = (df["macdsignal"] > df["macd"]) != (df["macdsignal"] > df["macd"]).shift(1)

    conditions = [
        ((df['macdcut'] == True) & (df['macdsignal'] < df["macd"]) & (df["macdhist"] > 0)),
        ((df['macdcut'] == True) & (df['macdsignal'] > df["macd"]) & (df["macdhist"] < 0))
    ]

    df["macd"] = np.select(conditions, [1, -1], default=0)
    df = df.drop(["macdsignal", "macdhist", "macdcut"], axis=1)
    return df


def rsi(df):
    df["rsi"] = talib.RSI(df["close"])
    df["rsicut"] = (df["rsi"] > 30) & (df["rsi"].shift(1) < 30) | (df["rsi"] < 70) & (df["rsi"].shift(1) > 70)

    conditions = [
        ((df["rsicut"] == True) & (df["rsi"] > 30) & (df["rsi"].shift(1) < 30)),
        ((df["rsicut"] == True) & (df["rsi"] < 70) & (df["rsi"].shift(1) > 70))
    ]

    df["rsi"] = np.select(conditions, [1, -1], default=0)
    df = df.drop("rsicut", axis=1)
    return df


def stoch(df):
    df["slowk"], df["slowd"] = talib.STOCH(df["high"], df["low"], df["close"])
    df["stochcut"] = (df["slowk"] > df["slowd"]) != (df["slowk"] > df["slowd"]).shift(1)

    conditions = [
        ((df['stochcut'] == True) & (df['slowk'] > df["slowd"]) & (df["slowd"] < 20)),
        ((df['stochcut'] == True) & (df['slowk'] < df["slowd"]) & (df["slowd"] > 80))
    ]

    df["stoch"] = np.select(conditions, [1, -1], default=0)
    df = df.drop(["slowk", "slowd", "stochcut"], axis=1)
    return df


def adx(df):
    df["adx"] = talib.ADX(df["high"], df["low"], df["close"])
    df["dm+"] = talib.PLUS_DM(df["high"], df["low"])
    df["dm-"] = talib.MINUS_DM(df["high"], df["low"])
    df["dmcut"] = (df["dm+"] > df["dm-"]) != (df["dm+"] > df["dm-"]).shift(1)

    conditions = [
        ((df["dmcut"] == True) & (df["adx"] > 25) & (df["dm+"] > df["dm-"])),
        ((df["dmcut"] == True) & (df["adx"] > 25) & (df["dm+"] < df["dm-"]))
    ]

    df["adx"] = np.select(conditions, [1, -1], default=0)
    df = df.drop(["dm+", "dm-", "dmcut"], axis=1)
    return df


def aroon(df):
    df["aroondown"], df["aroonup"] = talib.AROON(df["high"], df["low"], timeperiod=25)
    df["arooncut"] = (df["aroonup"] > df["aroondown"]) != (df["aroonup"] > df["aroondown"]).shift(1)

    conditions = [
        ((df['arooncut'] == True) & (df['aroonup'] > df["aroondown"])),
        ((df['arooncut'] == True) & (df['aroonup'] < df["aroondown"]))
    ]

    df["aroon"] = np.select(conditions, [1, -1], default=0)
    df = df.drop(["aroondown", "aroonup", "arooncut"], axis=1)
    return df


def bbands(df):
    df["upperband"], df["middleband"], df["lowerband"] = talib.BBANDS(df["close"], timeperiod=20)
    df["lowerbbandcut"] = (df["close"] > df["lowerband"]) != (df["close"] > df["lowerband"]).shift(1)
    df["upperbbandcut"] = (df["close"] > df["upperband"]) != (df["close"] > df["upperband"]).shift(1)

    conditions = [
        ((df['lowerbbandcut'] == True) & (df['close'] < df["lowerband"])),
        ((df['upperbbandcut'] == True) & (df['close'] > df["upperband"]))
    ]

    df["bbands"] = np.select(conditions, [1, -1], default=0)
    df = df.drop(["upperband", "middleband", "lowerband", "lowerbbandcut", "upperbbandcut"], axis=1)
    return df


def sar(df):
    df["sar"] = talib.SAR(df["high"], df["low"], acceleration=0.02, maximum=0.2)
    df["sarcut"] = (df["close"] > df["sar"]) != (df["close"] > df["sar"]).shift(1)

    conditions = [
        ((df["sarcut"] == True) & (df["close"] > df["sar"])),
        ((df["sarcut"] == True) & (df["close"] < df["sar"]))
    ]

    df["sar"] = np.select(conditions, [1, -1], default=0)
    df = df.drop("sarcut", axis=1)
    return df


def ma(df):
    df["ma15"] = talib.MA(df["close"], timeperiod=15)
    df["ma5"] = talib.MA(df["close"], timeperiod=5)
    df["macut"] = (df["ma5"] > df["ma15"]) != (df["ma5"] > df["ma15"]).shift(1)

    conditions = [
        ((df['macut'] == True) & (df['ma5'] > df["ma15"])),
        ((df['macut'] == True) & (df['ma5'] < df["ma15"]))
    ]

    df["ma"] = np.select(conditions, [1, -1], default=0)
    df = df.drop(["ma15", "ma5", "macut"], axis=1)
    return df


def forecast(df, forecast_period=30):
    df["forecast"] = ((df["close"].shift(-forecast_period)-df["close"])/df["close"])*100
    return df


def ohlcvish(df):
    FUNCTIONS = [
        macd,
        rsi,
        stoch,
        adx,
        aroon,
        bbands,
        sar,
        ma
    ]
    for f in FUNCTIONS:
        df = f(df)

    return df


if __name__ == "__main__":
    btc = pd.read_csv("./BTCUSD.csv")
    btc = ohlcvish(btc)
    print(btc)
