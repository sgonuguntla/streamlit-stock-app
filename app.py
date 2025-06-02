import yfinance as yf
import pandas as pd
import streamlit as st

st.title("Averages")

ticker = st.text_input("Enter Stock Symbol:", "AAPL")
start = st.text_input("Start Date:", "2023-01-01")
end = st.text_input("End Date:", "2024-12-31")

if st.button("Show Chart"):
    data = yf.download(ticker, start=start, end=end)

    # Debug print
    st.write("Raw Data:", data.head())

    if data.empty:
        st.error("No data found. Please check the stock symbol or date range.")
    else:
        if 'Close' not in data.columns:
            st.error("‘Close’ column not found in the data.")
        else:
            data['MA20'] = data['Close'].rolling(window=20).mean()
            data['MA50'] = data['Close'].rolling(window=50).mean()

            # Debug print
st.write("Processed Data:", data[['Close', 'MA20', 'MA50']].dropna().tail())

# Only plot if all required columns exist and have data
if all(col in data.columns for col in ['Close', 'MA20', 'MA50']) and not data[['Close', 'MA20', 'MA50']].dropna().empty:
    st.line_chart(data[['Close', 'MA20', 'MA50']].dropna())
else:
    st.warning("Not enough data to plot the chart. Try a larger date range.")
    
                     
