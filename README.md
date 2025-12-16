Crypto Market Insights Dashboard

An interactive cryptocurrency analytics dashboard built using Python and Streamlit that delivers real-time and historical market insights through quantitative analysis and intuitive visualizations.

Features
Live and historical cryptocurrency price analysis
Interactive candlestick and volume charts.
Key market metrics including price, volume, and daily range.
Quantitative analytics such as price spread, Z-score, and rolling correlation.
Z-score–based alert system to detect abnormal price movements.

Export analytical data as CSV for offline analysis

Tech Stack
Python
Streamlit
Plotly
Pandas, NumPy
Coinbase Exchange API


Frontend: Streamlit-based user interface for interaction and visualization
Data Source: Coinbase Exchange API for real-time and historical OHLCV data
Processing Layer: Data resampling, indicator computation, and quantitative analytics
Visualization Layer: Interactive Plotly charts for market trends and metrics
Alerts & Export: Threshold-based alerts and downloadable analytics data

How to Run the Project

Clone the repository

git clone https://github.com/your-username/crypto-market-insights-dashboard.git


Navigate to the project directory

cd crypto-market-insights-dashboard


Install dependencies

pip install -r requirements.txt


Run the Streamlit application

python -m streamlit run app.py


Open the browser link displayed in the terminal to access the dashboard.

Usage

Select the trading pair, timeframe, and sampling interval from the sidebar

Monitor real-time price movements and market metrics

Adjust the Z-score threshold to trigger anomaly alerts

Download analytics data for further offline analysis

Project Highlights

End-to-end data pipeline from API ingestion to visualization

Real-time quantitative analysis with user-controlled parameters

Clean and intuitive UI inspired by financial market dashboards
