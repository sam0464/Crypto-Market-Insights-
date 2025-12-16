Crypto Market Insights Dashboard
is a real-time cryptocurrency quantitative analytics dashboard designed to help traders, analysts, and researchers explore short-term market behavior using statistical indicators and interactive visualizations.

The dashboard emphasizes quantitative analysis, statistical signals, and alerting, rather than price prediction. This makes it suitable for exploratory analysis, signal generation, and research-oriented workflows.

🚀 Features
📈 Market Visualization

Interactive candlestick charts displaying OHLC (Open, High, Low, Close) prices

Volume bars aligned with price movements

Zoom, pan, and hover support using Plotly for detailed inspection

⏱️ Timeframe & Sampling Control
Timeframe Selection

Last 24 Hours

Last 3 Days

Last Week

Last Month

Sampling / Resampling Options

Raw (original market data)

1 Minute

5 Minutes

This separation allows flexible analysis across different historical spans and data resolutions.

📊 Quantitative Analytics

Spread
Measures short-term price deviation using lagged prices

Z-Score
Standardizes spread values to detect statistically significant deviations

Rolling Correlation
Tracks short-term dependency between consecutive price movements

🚨 Alerting System

Z-score–based anomaly alerts

User-defined threshold

Alert triggered when:
|Z| > threshold

Useful for mean-reversion strategies and anomaly detection.

📁 Data Export

Download processed data (prices + analytics) as CSV

Enables offline analysis and further research

🧱 Project Structure
project-folder/
│
├── app.py        # Streamlit dashboard (UI + analytics logic)
├── README.md     # Project documentation

🛠️ Tech Stack

Language: Python

Frontend & Backend: Streamlit

Data Source: Coinbase Exchange REST API

Data Processing: Pandas, NumPy

Visualization: Plotly

HTTP Requests: Requests

🔄 Data Flow & Methodology
1️⃣ Data Ingestion

Historical OHLCV data and latest ticker prices are fetched from the Coinbase Exchange REST API

No authentication or API keys required

2️⃣ Sampling / Resampling

Raw market data can be resampled into:

1-minute intervals

5-minute intervals

Aggregation logic:

Open → first value

High → maximum

Low → minimum

Close → last value

Volume → sum

3️⃣ Quantitative Analytics
🔹 Spread
Spread = Price(t) − Price(t−1)


Captures short-term price deviations useful for statistical monitoring.

🔹 Z-Score
Z = (Spread − Rolling Mean) / Rolling Standard Deviation


Used to identify statistically extreme price movements.

🔹 Rolling Correlation

Measures correlation between the current price and its lagged value

Helps identify regime changes or weakening trends

4️⃣ Alerting Logic

User defines a Z-score threshold

Alert is triggered when:

|Z| > Threshold

5️⃣ Visualization

Candlestick and volume charts

Z-score and rolling correlation plots

Fully interactive using Plotly

▶️ How to Run the Application
Install Dependencies
pip install streamlit pandas plotly requests numpy

Run the Application
python -m streamlit run app.py


The dashboard will open at:

http://localhost:8501

🧠 Design Philosophy

Clear separation between:

Data ingestion

Sampling

Analytics

Visualization

Designed for extensibility:

REST API → WebSocket upgrade possible

New quantitative indicators can be added easily

Focus on clarity, transparency, and analytical insight over complexity

An architecture diagram will be added in a future update.

🤖 ChatGPT Usage Transparency

ChatGPT was used as a development assistant for:

Structuring the application architecture

Generating and refining Python code

Validating analytics logic

Improving documentation clarity

All final implementation, testing, and design decisions were performed by the author.

🔮 Future Enhancements

WebSocket-based tick data ingestion

Multi-asset pair analytics

ADF stationarity testing

Kalman filter–based hedge ratio estimation

Mean-reversion backtesting module

Persistent storage using Redis or PostgreSQL

⚠️ Disclaimer

This project is intended solely for educational and research purposes.
It does not constitute financial, trading, or investment advice.
