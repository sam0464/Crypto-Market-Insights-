Crypto Market Insights Dashboard

An interactive cryptocurrency analytics dashboard built using Python and Streamlit that provides real-time market insights.

Features

Live and historical crypto price analysis

Interactive candlestick and volume charts

Key market metrics: price, volume, daily range

Quantitative analytics: spread, Z-score, rolling correlation

Z-score based alert system for abnormal price movement

Export analytics data as CSV

Tech Stack

Python

Streamlit

Plotly

Pandas, NumPy

Coinbase Exchange API

Architecture Overview

Frontend: Streamlit UI for user interaction and visualization

Data Source: Coinbase API for real-time and historical OHLCV data

Processing Layer: Data resampling, indicator calculation, quant analytics

Visualization: Interactive Plotly charts

Alerts & Export: Threshold-based alerts and CSV download

How to Run the Project

Clone the repository:

git clone https://github.com/your-username/crypto-market-insights-dashboard.git


Navigate to the project folder:

cd crypto-market-insights-dashboard


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

python -m streamlit run app.py


Open the browser link shown in the terminal to view the dashboard.

Usage

Select trading pair, timeframe, and sampling interval from the sidebar

Monitor real-time metrics and price movements

Use the Z-score slider to trigger anomaly alerts

Download analytics data for offline analysis

Project Highlights

End-to-end data pipeline from API ingestion to visualization

Real-time analytics with user-driven controls

Clean UI inspired by financial market dashboards