import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# Generate dates for each day in 2025
start_date = datetime(2025, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(365)]

# Generate realistic fitness data
steps = np.random.normal(loc=8500, scale=3000, size=365).clip(3000, 18000)
sleep_hours = np.random.normal(loc=7.2, scale=1, size=365).clip(4.5, 9.5)
heart_rate_bpm = np.random.normal(loc=68, scale=10, size=365).clip(48, 110)
calories_burned = np.random.randint(1800, 2401, size=365)
active_minutes = np.random.randint(20, 181, size=365)

# Create DataFrame
data = pd.DataFrame({
    'date': dates,
    'steps': steps,
    'sleep_hours': sleep_hours,
    'heart_rate_bpm': heart_rate_bpm,
    'calories_burned': calories_burned,
    'active_minutes': active_minutes
})

# Introduce 5% NaN values randomly
def introduce_nan(df, column_name):
    nan_indices = np.random.choice(df.index, size=int(len(df) * 0.05), replace=False)
    df.loc[nan_indices, column_name] = np.nan

for column in data.columns[1:]:  # Exclude 'date' from NaN introduction
    introduce_nan(data, column)

# Save the data to a CSV file
data.to_csv('data/health_data.csv', index=False)