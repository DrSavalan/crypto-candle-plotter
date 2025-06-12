# main.py

from crypto_plotter import create_dataframe, candlePlot

def main():
    share = 'BTC'            # or 'ETH', 'SOL', etc.
    tf = '1h'                # timeframe like '1m', '5m', '1h', '1d'
    seconds = 3600 * 100     # last 100 hours = 100 candles of 1h
    backsec = 0              # how far to look back from now

    df = create_dataframe(share, tf, seconds, backsec)
    candlePlot(df, f'{share}-{tf}')

if __name__ == '__main__':
    main()
