
import yfinance as yf
import pandas as pd
import streamlit as st

st.title("📈 Stock Price and Moving Averages")

# User inputs
ticker = st.text_input("Enter Stock Symbol:", "AAPL")
start = st.date_input("Start Date:", pd.to_datetime("2023-01-01"))
end = st.date_input("End Date:", pd.to_datetime("2024-12-31"))

if st.button("Show Chart"):
    data = yf.download(ticker, start=start, end=end)
    if data.empty:
        st.warning("No data found for the given inputs.")
    else:
        data['MA20'] = data['Close'].rolling(window=20).mean()
        data['MA50'] = data['Close'].rolling(window=50).mean()
        st.line_chart(data[['Close', 'MA20', 'MA50']])
