import yfinance as yf
import pandas as pd
import streamlit as st

st.title("Averages")

ticker = st.text_input("Enter Stock Symbol:", "AAPL")
start = st.text_input("Start Date:", "2023-01-01")
end = st.text_input("End Date:", "2024-12-31")

if st.button("Show Chart"):
    data = yf.download(ticker, start=start, end=end)

    if data.empty:
        st.error("No data found. Please check the stock symbol or date range.")
        st.stop()

    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()

    st.line_chart(data[['Close', 'MA20', 'MA50']])
