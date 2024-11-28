import streamlit as st
import requests
import numpy as np
import plotly.graph_objs as go
import time
from datetime import datetime

# Ngrok public URL for your local server
ngrok_url = "https://8351-2407-d000-f-bce6-6dc8-f949-b628-8b5e.ngrok-free.app/get_samples"

st.title("Remote INMP441 Audio Data Viewer")
st.write("Fetching data from the local server exposed via Ngrok...")

# Initialize placeholders for the plot and elapsed time
plotly_chart_placeholder = st.empty()
last_transfer_time = st.empty()

# Function to fetch data from the Ngrok URL
def fetch_data():
    try:
        response = requests.get(ngrok_url, timeout=5)
        if response.status_code == 200:
            # Parse JSON data
            data = response.json()
            # Convert list to numpy array
            samples = np.array(data, dtype=np.int16)
            return samples
        else:
            st.error(f"Error: Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

# Track the last data fetch time
last_fetch_time = None

# Continuously fetch data and update the plot
while True:
    samples = fetch_data()
    
    if samples is not None and len(samples) > 0:
        last_fetch_time = datetime.now()  # Update the last fetch time
        # Create a new Plotly figure
        fig = go.Figure(data=[go.Scatter(y=samples, mode='lines', name='I2S Data')])
        fig.update_layout(
            title="Real-time I2S Data Plot",
            xaxis_title="Samples",
            yaxis_title="Amplitude",
            xaxis=dict(range=[0, len(samples)]),  # Update X-axis dynamically based on data length
            yaxis=dict(range=[-32768, 32767])  # 16-bit audio range
        )
        # Update the placeholder with a unique key for each update
        plotly_chart_placeholder.plotly_chart(fig, use_container_width=True, key=f"plot_{datetime.now().timestamp()}")

    # Display the elapsed time since the last successful data transfer
    if last_fetch_time:
        elapsed_time = (datetime.now() - last_fetch_time).total_seconds()
        last_transfer_time.write(f"Seconds since last data transfer: {elapsed_time:.2f}")

    time.sleep(5)  # Adjust the frequency of fetching data as needed
