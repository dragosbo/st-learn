import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# App title and description
st.title("Time Series Visualizer")
st.write("A simple demonstration of time series visualization with Streamlit")

# Generate sample time series data
def generate_time_series(days=90, trend=0.1, seasonality=10, noise=1.0):
    dates = [datetime.now() - timedelta(days=i) for i in range(days)]
    dates.reverse()
    
    # Create time series with trend, seasonality and noise
    values = [trend * i + seasonality * np.sin(i * np.pi / 7) + noise * np.random.randn() 
              for i in range(days)]
    
    df = pd.DataFrame({
        'date': dates,
        'value': values
    })
    return df

# Sidebar controls
st.sidebar.header("Data Parameters")
days = st.sidebar.slider("Number of days", 30, 365, 90)
trend = st.sidebar.slider("Trend factor", -0.5, 0.5, 0.1, 0.01)
seasonality = st.sidebar.slider("Seasonality factor", 0.0, 20.0, 10.0, 0.5)
noise = st.sidebar.slider("Noise factor", 0.0, 5.0, 1.0, 0.1)

# Generate data
df = generate_time_series(days, trend, seasonality, noise)

# Display the data
st.subheader("Sample Time Series Data")
st.dataframe(df.head())

# Visualize the data
st.subheader("Time Series Visualization")
fig = px.line(df, x='date', y='value', title='Time Series Data')
fig.update_layout(xaxis_title="Date", yaxis_title="Value")
st.plotly_chart(fig, use_container_width=True)

# Add rolling average
st.subheader("Rolling Average")
window_size = st.slider("Window size for rolling average", 1, 30, 7)
df['rolling_avg'] = df['value'].rolling(window=window_size).mean()

# Plot original and rolling average
fig2 = px.line(df, x='date', y=['value', 'rolling_avg'], 
              title=f'Original vs {window_size}-day Rolling Average')
fig2.update_layout(xaxis_title="Date", yaxis_title="Value", 
                  legend_title="Metric")
st.plotly_chart(fig2, use_container_width=True)

# Add a download button for the data
csv = df.to_csv(index=False)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="time_series_data.csv",
    mime="text/csv",
)

st.info("This app demonstrates a simple time series visualization deployed on Streamlit Community Cloud for free.")
