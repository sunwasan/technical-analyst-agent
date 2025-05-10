# Stock Technical Analysis Agent

This project implements a technical analysis agent for stock trading using AI-powered chart analysis. The agent analyzes stock charts using technical indicators and provides trading recommendations based on the visual patterns detected.

## Overview

The technical analysis agent:
1. Fetches historical stock data using yfinance
2. Calculates technical indicators (RSI, MACD, SMA)
3. Generates visualizations with candlestick charts and indicators
4. Uses Google's Gemini AI to analyze the charts
5. Provides trading recommendations with entry points, stop loss, and take profit levels
6. Backtests the strategy on historical data to evaluate performance

## Key Features

- **Visual Stock Analysis**: Generate comprehensive stock charts with price, volume, RSI, and MACD indicators
- **AI-Powered Technical Analysis**: Utilize Google's Gemini AI model to interpret chart patterns and provide trading insights
- **Backtesting Framework**: Test the AI agent's recommendations on historical data to evaluate performance
- **Customizable Parameters**: Adjust technical indicators and timeframes based on your trading strategy

## Project Structure

- `plot_stock_analysis.py`: Visualization module for creating technical analysis charts
- `ta_agent.ipynb`: Jupyter notebook containing the technical analysis agent implementation and backtesting framework
- `requirements.txt`: List of required Python packages

## Requirements

- Python 3.8+
- Google Gemini API key (store in `.env` file)

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

### Running the Technical Analysis Agent

1. Open `ta_agent.ipynb` in Jupyter Notebook or VS Code
2. Configure the stock symbol and date range:
   ```python
   symbol = "CPALL.BK"  # Change to your desired stock symbol
   start_date = "2023-01-01"  # Adjust the start date as needed
   ```
3. Run all cells in the notebook to execute the backtest

### Stock Chart Visualization

You can use the `plot_stock_analysis` function independently:

```python
import yfinance as yf
from plot_stock_analysis import plot_stock_analysis

# Download stock data
symbol = "AAPL"
start_date = "2023-01-01"
data = yf.download(symbol, start=start_date)

# Generate and display stock chart
fig = plot_stock_analysis(data, symbol)
fig.show()
```

## Technical Indicators

The stock charts include:
- **Price**: Candlestick chart with open, high, low, and close prices
- **Volume**: Trading volume over time
- **SMA**: 20-day and 50-day Simple Moving Averages
- **RSI**: Relative Strength Index with overbought/oversold levels
- **MACD**: Moving Average Convergence Divergence with signal line

## Backtest Methodology

The backtesting process:
1. Selects multiple random points in the historical data
2. Generates technical analysis charts up to each selected point
3. Obtains trading recommendations from the AI agent
4. Simulates trades based on the recommendations over a 1-month period
5. Calculates returns and statistics for performance evaluation

## License

[Specify license information here]

## Disclaimer

This software is for educational and research purposes only. It is not intended to provide investment advice. Always consult with a qualified financial advisor before making investment decisions.
