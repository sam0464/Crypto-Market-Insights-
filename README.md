Crypto Market Insights Dashboard

The MarketLens Quant Analytics Dashboard is a real-time cryptocurrency market analytics tool designed to help traders and researchers monitor price behavior, statistical signals, and short-term market dynamics.

The dashboard focuses on quantitative analytics, statistical indicators, and alerting, rather than price prediction, making it suitable for exploratory analysis, signal generation, and research workflows.

🚀 Features 📈 Market Visualization

Candlestick Chart showing OHLC (Open, High, Low, Close) prices

Volume Bars aligned with price action

Interactive charts with zoom, pan, and hover support

⏱️ Timeframe & Sampling Control

Timeframe Selection:

Last 24 Hours

Last 3 Days

Last Week

Last Month

Sampling / Resampling Options:

Raw (original data)

1 Minute

5 Minutes

This separation allows flexible analysis across different historical spans and resolutions.

📊 Quantitative Analytics

Spread

Measures short-term price deviation using lagged prices

Z-Score

Standardizes spread values to identify statistically significant deviations

Rolling Correlation

Tracks short-term dependency between consecutive price movements

🚨 Alerting

Z-Score Threshold Alerts

User-defined threshold

Alert triggered when |Z| > threshold

Useful for mean-reversion and anomaly detection

📁 Data Export

Download processed data (prices + analytics) as CSV

Enables offline analysis and research

🧱 Project Structure project-folder/ ├── app.py # Streamlit dashboard (frontend + backend logic) ├── README.md # Project documentation

🛠️ Tech Stack

Language: Python

Frontend & Backend: Streamlit

Data Source: Coinbase Exchange REST API

Data Processing: Pandas, NumPy

Visualization: Plotly

HTTP Requests: Requests

🔄 Data Flow & Methodology 1️⃣ Data Ingestion

Historical OHLCV data and latest ticker prices are fetched from the Coinbase Exchange REST API

No authentication or API keys required

2️⃣ Sampling / Resampling

Raw market data can be resampled to:

1-minute

5-minute intervals

Aggregation logic:

Open → first value

High → max

Low → min

Close → last

Volume → sum

3️⃣ Quantitative Analytics 🔹 Spread Spread = Price(t) − Price(t−1)

Captures short-term deviations useful for statistical monitoring.

🔹 Z-Score Z = (Spread − Rolling Mean) / Rolling Standard Deviation

Used to detect statistically extreme price movements.

🔹 Rolling Correlation

Measures correlation between current price and its lagged version

Helps identify regime changes or weakening trends

4️⃣ Alerting Logic

User defines a Z-score threshold

Alert is triggered when:

|Z| > Threshold

5️⃣ Visualization

Candlestick + volume charts

Z-score and correlation plots

Fully interactive using Plotly

▶️ How to Run the Application

Install Dependencies pip install streamlit pandas plotly requests numpy

Run the App python -m streamlit run app.py

The dashboard will open at:

http://localhost:8501

🧠 Design Philosophy

Modular separation between:

Data ingestion

Sampling

Analytics

Visualization

Designed for extensibility:

REST → WebSocket upgrade possible

New analytics can be added easily

Focus on clarity over complexity

An architecture diagram will be added in a future update.

🤖 ChatGPT Usage Transparency

ChatGPT was used as a development assistant for:

Structuring the application architecture

Generating and refining Python code

Validating analytics logic

Improving documentation clarity

All final implementation, testing, and decisions were performed by the author.

🔮 Future Enhancements

WebSocket-based tick data ingestion

Multi-asset pair analytics

ADF stationarity testing

Kalman filter-based hedge ratio

Mean-reversion backtesting module

Persistent storage using Redis or PostgreSQL

⚠️ Disclaimer

This project is intended for educational and research demonstration purposes only and does not constitute financial or investment advice.
