# fetcher.py

import datetime
import pandas as pd
from binance.client import Client
from .config import my_API_Key, my_API_Secret

def give(shareName, timeframe, seconds, backsec):
    symbol = shareName + 'USDT'
    end = datetime.datetime.now()
    end = int(end.timestamp() * 1000) - backsec * 1000
    start = end - seconds * 1000
    client = Client(my_API_Key, my_API_Secret)
    klines = client.get_historical_klines(symbol=symbol, interval=timeframe, start_str=start, end_str=end)
    return klines

def create_dataframe(shareName, timeframe, seconds, backsec):  
    data = give(shareName, timeframe, seconds, backsec)
    df = pd.DataFrame(data, columns=[
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume',
        'Close Time', 'Quote asset volume', 'Number of trades',
        'Taker buy base asset volume', 'Taker buy quote asset volume', 'Ignore'
    ])
    df['Datetime'] = pd.to_datetime(df['Open Time'], unit='ms')
    df.index = df['Datetime']
    df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[['Open', 'High', 'Low', 'Close', 'Volume']].astype(float)
    return df
