import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import seaborn as sns
from mpl_finance import candlestick_ohlc

def plot_stock_analysis(df, symbol, rsi_window=14):
    # --- Preprocessing ---
    b_df = df.reset_index()
    b_df.columns = b_df.columns.str.lower()
    b_df['date'] = pd.to_datetime(b_df['date'])
    b_df['date_num'] = b_df['date'].apply(mpl_dates.date2num)

    # OHLC
    ohlc = b_df[['date_num', 'open', 'high', 'low', 'close']].astype(float)

    # --- Plotting ---
    sns.set(style="whitegrid")
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(18, 9), sharex=True,
                                             gridspec_kw={'height_ratios': [3, 1, 1, 1]})

    # 1. Candlestick chart
    ax1.set_title(symbol)
    ax1.set_ylabel("Price")
    candlestick_ohlc(ax1, ohlc.values, width=0.6, colorup='green',
                     colordown='red', alpha=0.6)

    # SMA
    short_sma = b_df['close'].rolling(window=20).mean()
    long_sma = b_df['close'].rolling(window=50).mean()
    ax1.plot(b_df['date_num'], short_sma, label='20-day SMA', color='blue')
    ax1.plot(b_df['date_num'], long_sma, label='50-day SMA', color='orange')
    ax1.fill_between(b_df['date_num'], short_sma, long_sma, 
                     where=(short_sma > long_sma), facecolor='green', alpha=0.3)
    ax1.fill_between(b_df['date_num'], short_sma, long_sma, 
                     where=(short_sma < long_sma), facecolor='red', alpha=0.3)

    # Price markers
    ax1.axhline(b_df['close'].iloc[0], linestyle='--', alpha=0.5, color='black')
    ax1.text(b_df['date_num'].iloc[0], b_df['close'].iloc[0],
             f"Start: {b_df['close'].iloc[0]:.2f}", fontsize=10, color='black')
    ax1.axhline(b_df['close'].iloc[-1], linestyle='--', alpha=0.5, color='black')
    ax1.text(b_df['date_num'].iloc[-1], b_df['close'].iloc[-1],
             f"End: {b_df['close'].iloc[-1]:.2f}", fontsize=10, color='black')
    ax1.text(b_df['date_num'].iloc[-1], b_df['close'].iloc[-1] * 1.02,
             f"Change: {b_df['close'].iloc[-1] - b_df['close'].iloc[0]:.2f}", fontsize=10, color='black')
    ax1.set_ylim(b_df['low'].min() * 0.95, b_df['high'].max() * 1.05)
    ax1.legend()

    # 2. Volume
    ax2.set_ylabel("Volume")
    ax2.bar(b_df['date_num'], b_df['volume'], width=1, color='blue', alpha=0.3)

    # 3. RSI
    ax3.set_ylabel("RSI")
    ax3.plot(b_df['date_num'], b_df['rsi'], label='RSI', color='purple')
    ax3.axhline(70, linestyle='--', alpha=0.5, color='red', label='Overbought')
    ax3.axhline(50, linestyle='--', alpha=0.5, color='black', label='Neutral')
    ax3.axhline(30, linestyle='--', alpha=0.5, color='green', label='Oversold')
    ax3.fill_between(b_df['date_num'], b_df['rsi'], 70, 
                     where=(b_df['rsi'] > 70), facecolor='red', alpha=0.3)
    ax3.fill_between(b_df['date_num'], b_df['rsi'], 30, 
                     where=(b_df['rsi'] < 30), facecolor='green', alpha=0.3)
    ax3.fill_between(b_df['date_num'], b_df['rsi'], 50, 
                     where=(b_df['rsi'] > 50), facecolor='blue', alpha=0.3)
    ax3.fill_between(b_df['date_num'], b_df['rsi'], 50, 
                     where=(b_df['rsi'] < 50), facecolor='orange', alpha=0.3)
    ax3.legend(loc='upper left')
    
    ax3.set_ylim(0, 100)

    # 4. MACD
    ax4.set_ylabel("MACD")
    ax4.plot(b_df['date_num'], b_df['macd'], label='MACD', color='blue')
    ax4.plot(b_df['date_num'], b_df['signal'], label='Signal', color='orange')
    ax4.fill_between(b_df['date_num'], b_df['macd'] - b_df['signal'], 0, 
                     where=(b_df['macd'] - b_df['signal']) > 0, facecolor='green', alpha=0.3)
    ax4.fill_between(b_df['date_num'], b_df['macd'] - b_df['signal'], 0, 
                     where=(b_df['macd'] - b_df['signal']) < 0, facecolor='red', alpha=0.3)
    ax4.legend(loc='upper left')

    # X-axis formatting
    date_format = mpl_dates.DateFormatter('%Y-%m-%d')
    ax4.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()

    # plt.show()
    return fig