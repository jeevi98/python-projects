import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import sys

def fetch_stock_data(symbol, start_date, end_date):
    try:
        print(f"\n Fetching data for {symbol} from {start_date} to {end_date}...")
        stock = yf.download(symbol, start=start_date, end=end_date)
        if stock.empty:
            print(" No data found. Check symbol or date range.")
            return None
        return stock
    except Exception as e:
        print(f" Error fetching stock data: {e}")
        return None

def plot_stock_data(df, symbol):
    try:
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
        plt.title(f"{symbol} - Closing Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price (₹)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"{symbol}_closing_price.png")
        print(f" Saved: {symbol}_closing_price.png")

        plt.figure(figsize=(12, 4))
        plt.bar(df.index, df['Volume'], label='Volume', color='green')
        plt.title(f"{symbol} - Trading Volume")
        plt.xlabel("Date")
        plt.ylabel("Volume")
        plt.tight_layout()
        plt.savefig(f"{symbol}_volume.png")
        print(f" Saved: {symbol}_volume.png")

    except Exception as e:
        print(f" Error plotting data: {e}")

def main():
    print(" Stock Price Analyzer (using yfinance)\n")

    symbol = input("Enter stock symbol (e.g., INFY.NS, TCS.NS, AAPL): ").strip().upper()
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    df = fetch_stock_data(symbol, start_date, end_date)

    if df is not None:
        print("\n Data Preview:\n")
        print(df[['Open', 'High', 'Low', 'Close', 'Volume']].head())

        plot_stock_data(df, symbol)

if __name__ == "__main__":
    main()
