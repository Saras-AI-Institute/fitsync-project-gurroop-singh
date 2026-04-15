import streamlit as st
import plotly.express as px
from modules.processor import process_data

# Set page configurations
st.set_page_config(layout="wide", page_title="FitSync")

# Main title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Sidebar filters
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 days", "Last 30 days", "All time"],
    index=2
)

# Load and process the data
df = process_data()

# Filter the DataFrame based on time range
if time_range == "Last 7 days":
    filtered_df = df.tail(7)
elif time_range == "Last 30 days":
    filtered_df = df.tail(30)
else:
    filtered_df = df  # "All time" uses the full DataFrame

# Create a three-column layout
col1, col2, col3 = st.columns(3)

# Calculate metrics
avg_steps = filtered_df['steps'].mean()
avg_sleep_hours = filtered_df['sleep_hours'].mean()
avg_recovery_score = filtered_df['recovery_score'].mean()

# Display metrics
with col1:
    st.metric(label="Average Steps", value=f"{avg_steps:.0f}", delta=None)
with col2:
    st.metric(label="Average Sleep Hours", value=f"{avg_sleep_hours:.1f}", delta=None)
with col3:
    st.metric(label="Average Recovery Score", value=f"{avg_recovery_score:.1f}", delta=None)

# Dual line chart: Recovery Score & Sleep Trend
dual_chart = px.line(
    filtered_df, 
    x='date', 
    y=['recovery_score', 'sleep_hours'], 
    labels={'value': 'Scores', 'variable': 'Metrics'},
    title="Recovery Score & Sleep Trend"
)

# Scatter plot: Recovery score vs Steps
scatter_plot = px.scatter(
    filtered_df, 
    x='steps', 
    y='recovery_score', 
    color='sleep_hours', 
    labels={'color': 'Sleep Hours'},
    title="Recovery Score vs Daily Steps"
)

# Align charts in a two-column layout
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(dual_chart, use_container_width=True)
with col2:
    st.plotly_chart(scatter_plot, use_container_width=True)

# Scatter plot: Recovery score vs Resting heart rate
scatter_hr_chart = px.scatter(
    filtered_df,
    x='heart_rate_bpm',
    y='recovery_score',
    labels={'y': 'Recovery Score', 'x': 'Heart Rate (BPM)'},
    title="Recovery Score vs Resting Heart Rate"
)

# Line chart: Daily calories burnt trend
calories_burnt_chart = px.line(
    filtered_df,
    x='date',
    y='calories_burned',
    title="Daily Calories Burnt Trend"
)

# Align charts in a two-column layout
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(scatter_hr_chart, use_container_width=True)
with col2:
    st.plotly_chart(calories_burnt_chart, use_container_width=True)

# Placeholder for further sections
st.markdown("### Insights & Analytics")
# Add insightful analytics and charts here

st.markdown("---")
st.markdown("*Empower your health journey with data-driven insights.*")

# Additional sections or features can be added here as needed