import streamlit as st
import requests
import numpy as np
import plotly.graph_objs as go
from datetime import datetime
import time

# Ngrok public URL for your local server
ngrok_url = "https://8351-2407-d000-f-bce6-6dc8-f949-b628-8b5e.ngrok-free.app/get_samples"

st.title("Remote INMP441 Audio Data Viewer")
st.write("Fetching data from the local server exposed via Ngrok...")

# Placeholder for the plot and timestamp
plotly_chart = st.empty()
last_packet_time = st.empty()

# Plotly figure setup (initial empty plot)
fig = go.Figure()
fig.update_layout(
    title="Real-time I2S Data Plot",
    xaxis_title="Samples",
    yaxis_title="Amplitude",
    xaxis=dict(range=[0, 1024]),  # X-axis range is fixed to 1024 samples
    yaxis=dict(range=[-32768, 32767])  # Adjust Y-axis for 16-bit audio
)

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

# Continuously fetch data and update the plot
while True:
    samples = fetch_data()
    
    if samples is not None and len(samples) > 0:
        # Update the figure with new data
        fig.data = []  # Clear existing data
        fig.add_trace(go.Scatter(y=samples, mode='lines', name='I2S Data'))
        fig.update_layout(
            xaxis=dict(range=[0, len(samples)])  # Update X-axis dynamically based on data length
        )
        # Dynamically update the plot
        plotly_chart.plotly_chart(fig, use_container_width=True)
        
        # Update timestamp
        last_packet_time.write(f"Last packet received at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.write("No data available")

    time.sleep(5)  # Adjust the frequency of fetching data as needed
