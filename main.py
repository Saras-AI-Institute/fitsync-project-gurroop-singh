import streamlit as st
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

# Create a three-column layout
col1, col2, col3 = st.columns(3)

# Load and process the data
try:
    df = process_data()

    # Filter the DataFrame based on time range
    if time_range == "Last 7 days":
        df = df.tail(7)
    elif time_range == "Last 30 days":
        df = df.tail(30)
    # "All time" uses the full DataFrame, so no need to filter further

    # Calculate metrics
    avg_steps = df['steps'].mean()
    avg_sleep_hours = df['sleep_hours'].mean()
    avg_recovery_score = df['recovery_score'].mean()
    # Display metrics
    with col1:
        st.metric(label="Average Steps", value=f"{avg_steps:.0f}", delta=None)
    with col2:
        st.metric(label="Average Sleep Hours", value=f"{avg_sleep_hours:.1f}", delta=None)
    with col3:
        st.metric(label="Average Recovery Score", value=f"{avg_recovery_score:.1f}", delta=None)

    # Display the raw data
    st.header("Health Data Overview")
    st.dataframe(df)
    
    # More analysis and visualization can go here
    # ...

except Exception as e:
    st.error(f"An error occurred while processing data: {e}")

# Placeholder for further sections
st.markdown("### Insights & Analytics")
# Add insightful analytics and charts here, e.g.:
# st.bar_chart(data['recovery_score'])

st.markdown("---")
st.markdown("*Empower your health journey with data-driven insights.*")

# Additional sections or features can be added here as needed