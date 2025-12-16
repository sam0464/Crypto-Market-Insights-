import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta, timezone
import requests
import numpy as np


class CoinbaseAPI:
    BASE_URL = "https://api.exchange.coinbase.com"

    def get_ticker(self, product_id):
        url = f"{self.BASE_URL}/products/{product_id}/ticker"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()

    def get_historical_data(self, product_id, days):
        end = datetime.now(timezone.utc)
        start = end - timedelta(days=days)

        params = {
            "start": start.isoformat(),
            "end": end.isoformat(),
            "granularity": 3600  # 1 hour candles
        }

        url = f"{self.BASE_URL}/products/{product_id}/candles"
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()

        df = pd.DataFrame(
            r.json(),
            columns=["time", "low", "high", "open", "close", "volume"]
        )

        df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
        df = df.sort_values("time")
        return df


class LiveCryptoDashboard:
    def __init__(self):
        self.api = CoinbaseAPI()

   
    def resample_data(self, df, sampling):
        if sampling == "Raw":
            return df

        df = df.set_index("time")
        rule = "1T" if sampling == "1 Min" else "5T"

        df = df.resample(rule).agg({
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last",
            "volume": "sum"
        }).dropna()

        df = df.reset_index()
        return df

  
    def calculate_indicators(self, df):
        df["SMA20"] = df["close"].rolling(20).mean()
        df["EMA20"] = df["close"].ewm(span=20, adjust=False).mean()
        df["Daily_Range"] = df["high"] - df["low"]
        return df

   
    def compute_spread_zscore(self, price):
        shifted = price.shift(1)
        spread = price - shifted
        z = (spread - spread.rolling(20).mean()) / spread.rolling(20).std()
        return spread, z

    def rolling_corr(self, price):
        return price.rolling(20).corr(price.shift(1))

   
    def create_chart(self, df, pair):
        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            row_heights=[0.7, 0.3],
            vertical_spacing=0.03
        )

        fig.add_trace(go.Candlestick(
            x=df["time"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            name="OHLC",
            increasing_line_color="green",
            decreasing_line_color="red"
        ), row=1, col=1)

        colors = ["green" if c >= o else "red"
                  for c, o in zip(df["close"], df["open"])]

        fig.add_trace(go.Bar(
            x=df["time"],
            y=df["volume"],
            marker_color=colors,
            name="Volume"
        ), row=2, col=1)

        fig.update_layout(
            title=f"{pair} Market Analysis",
            xaxis_rangeslider_visible=False,
            height=700,
            template="plotly_white",
            paper_bgcolor="#f5f5f5",
            plot_bgcolor="#f5f5f5",
            font=dict(color="#222222"),
            xaxis=dict(showgrid=True, gridcolor="#e0e0e0"),
            yaxis=dict(showgrid=True, gridcolor="#e0e0e0"),
            yaxis2=dict(showgrid=True, gridcolor="#e0e0e0")
        )
        return fig

   
    def run_dashboard(self):
        st.set_page_config(
            page_title="Crypto Market Insights", layout="wide", initial_sidebar_state="expanded"
        )
        st.markdown("<h1 style='text-align:center; color:#0b3d91;'>📈 Crypto Market Insights Dashboard</h1>", unsafe_allow_html=True)
        st.sidebar.header("Controls")

        sampling = st.sidebar.selectbox("Sampling", ["Raw", "1 Min", "5 Min"])
        z_thresh = st.sidebar.slider("Z-score Alert", 1.0, 3.0, 2.0)

        pairs = ["BTC-USD", "ETH-USD", "SOL-USD", "ADA-USD"]
        pair = st.sidebar.selectbox("Trading Pair", pairs)

        days_map = {
            "Last 24 Hours": 1,
            "Last 3 Days": 3,
            "Last Week": 7,
            "Last Month": 30
        }
        tf = st.sidebar.selectbox("Timeframe", list(days_map.keys()))
        days = days_map[tf]

        
        df = self.api.get_historical_data(pair, days)
        df = self.resample_data(df, sampling)
        df = self.calculate_indicators(df)

        ticker = self.api.get_ticker(pair)
        current_price = float(ticker["price"])

        latest = df.iloc[-1]

        st.markdown("### Key Metrics")
        c1, c2, c3 = st.columns(3)
        c1.metric("💲 Current Price", f"${current_price:.2f}", delta=f"{((current_price - latest['open'])/latest['open'])*100:.2f}%")
        c2.metric("📊 Volume", f"{latest['volume']:.2f}")
        c3.metric("📈 Daily Range", f"{latest['Daily_Range']:.2f}")

        st.markdown("---")

       
        st.plotly_chart(self.create_chart(df, pair), use_container_width=True)

      
        spread, z = self.compute_spread_zscore(df["close"])
        corr = self.rolling_corr(df["close"])

        st.markdown("### Quantitative Analysis")
        col1, col2 = st.columns(2)

        with col1:
            fig_z = go.Figure()
            fig_z.add_trace(go.Scatter(x=df["time"], y=z, name="Z-score", line=dict(color="#0b3d91")))
            fig_z.update_layout(template="plotly_white", height=350,
                                paper_bgcolor="#f5f5f5", plot_bgcolor="#f5f5f5",
                                xaxis=dict(showgrid=True, gridcolor="#e0e0e0"),
                                yaxis=dict(showgrid=True, gridcolor="#e0e0e0"))
            st.plotly_chart(fig_z, use_container_width=True)

        with col2:
            fig_c = go.Figure()
            fig_c.add_trace(go.Scatter(x=df["time"], y=corr, name="Rolling Correlation", line=dict(color="#ff9900")))
            fig_c.update_layout(template="plotly_white", height=350,
                                paper_bgcolor="#f5f5f5", plot_bgcolor="#f5f5f5",
                                xaxis=dict(showgrid=True, gridcolor="#e0e0e0"),
                                yaxis=dict(showgrid=True, gridcolor="#e0e0e0"))
            st.plotly_chart(fig_c, use_container_width=True)

       
        if not z.dropna().empty and abs(z.iloc[-1]) > z_thresh:
            st.warning("🚨 Z-score Alert Triggered!")

       
        export_df = df.copy()
        export_df["Spread"] = spread
        export_df["Zscore"] = z
        export_df["Correlation"] = corr

        st.download_button(
            "Download Analytics CSV",
            export_df.to_csv(index=False).encode(),
            "analytics.csv"
        )

        st.caption(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    LiveCryptoDashboard().run_dashboard()
